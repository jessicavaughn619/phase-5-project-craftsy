import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')
app.config['GOOGLE_OAUTH_CLIENT_ID'] = os.environ.get('GOOGLE_OAUTH_CLIENT_ID')
app.config['GOOGLE_OAUTH_CLIENT_SECRET'] = os.environ.get('GOOGLE_OAUTH_CLIENT_SECRET')
app.config['OAUTHLIB_RELAX_TOKEN_SCOPE'] = os.environ.get('OAUTHLIB_RELAX_TOKEN_SCOPE')
app.config['OAUTHLIB_INSECURE_TRANSPORT'] = os.environ.get('OAUTHLIB_INSECURE_TRANSPORT')
app.json.compact = False

db = SQLAlchemy()
migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)
CORS(app)

