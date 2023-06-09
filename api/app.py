from flask import redirect, url_for, request, session, make_response, jsonify
from flask_restful import Api, Resource
from sqlalchemy.exc import IntegrityError

from config import app, db, google
from models import User

api = Api(app)

@app.route("/api/python")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/google/callback')
def google_callback():
    resp = google.authorized_response()
    if resp is None or 'access_token' not in resp:
        # Handle authorization failure
        return redirect(url_for('login'))

    access_token = resp['access_token']
    # Use the access_token to authenticate and authorize the user
    # ...

    # Redirect to a protected resource or perform any necessary actions
    return redirect(url_for('protected'))

@google.tokengetter
def get_google_oauth_token():
    return session.get('google_token')

class CheckSession(Resource):
    def get_session(self):
        if session.get('user_id'):
            user = User.query.filter(User.id == session['user_id']).first()
            return user.to_dict(), 200
        return {'error': '401 Unauthorized'}, 401

api.add_resource(CheckSession, '/api/check_session', endpoint='check_session')

