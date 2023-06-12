from flask import request, session, make_response, flash, redirect, url_for
from flask_restful import Api, Resource
from sqlalchemy.exc import IntegrityError, NoResultFound
from flask_login import current_user, login_user, logout_user
from flask_dance.contrib.google import google, make_google_blueprint
from flask_dance.consumer.storage.sqla import SQLAlchemyStorage

from config import app, db
from models import User, OAuth

api = Api(app)

blueprint = make_google_blueprint(
    scope=["email"],
    storage=SQLAlchemyStorage(OAuth, db.session, user=current_user)
)
app.register_blueprint(blueprint, url_prefix="/api/login")

@app.route("/api/home")
def index():
    return '<h1>Craftsy Back End Development</h1>'

@app.route("/api/logout")
def logout():
    logout_user()
    return redirect("/api/python")

class Users(Resource):
    def get(self):
        users = [user.to_dict() for user in User.query.all()]
        return make_response(users, 200)

# create/login local user on successful OAuth login
class GoogleLoginResource(Resource):
    def post(self):
        if not current_user.is_authenticated:
            flash("Failed to log in.", category="error")
            return {"success": False}, 401
        
        if not google.authorized:
            flash("Failed to log in.", category="error")
            return {"success": False}, 401

        resp = google.get("/oauth2/v1/userinfo")
        if not resp.ok:
            msg = "Failed to fetch user info."
            flash(msg, category="error")
            return {"success": False}, 500

        info = resp.json()
        user_id = info["id"]

        # Find this OAuth token in the database, or create it
        query = OAuth.query.filter_by(provider=blueprint.name, provider_user_id=user_id)
        try:
            oauth = query.one()
        except NoResultFound:
            oauth = OAuth(provider=blueprint.name, provider_user_id=user_id, token=google.token["access_token"])

        if oauth.user:
            login_user(oauth.user)
            flash("Successfully signed in.")

        else:
            # Create a new local user account for this user
            user = User(email=info["email"])
            # Associate the new local user account with the OAuth token
            oauth.user = user
            # Save and commit our database models
            db.session.add_all([user, oauth])
            db.session.commit()
            # Log in the new local user account
            login_user(user)
            flash("Successfully signed in.")

        return {"success": True}, 200


# notify on OAuth provider error
class GoogleErrorResource(Resource):
    def post(self):
        message = request.form.get("message")
        response = request.form.get("response")
        msg = f"OAuth error from Google! message={message} response={response}"
        flash(msg, category="error")
        return {"success": True}, 200

api.add_resource(GoogleLoginResource, '/api/login', endpoint="api/login")
api.add_resource(GoogleErrorResource, '/api/error')
api.add_resource(Users, '/api/users', endpoint='users')