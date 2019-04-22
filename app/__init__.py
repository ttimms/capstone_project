from flask import Flask
from flask_mail import Mail
from twilio.rest import Client
from config import Config
import os
from twilio.http.http_client import TwilioHttpClient
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

# setting up sqlalchemy and db migrations
sqlAlchemy_db = SQLAlchemy(app)
migrate = Migrate(app, sqlAlchemy_db)

# setup for login management
login = LoginManager(app)
login.login_view = 'login'

# setup object for email notification
mail = Mail(app)

# setup object for sms notification
proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}
sms_client = Client(
                Config.SMS_ACCOUNT_SID,
                Config.SMS_AUTH_TOKEN,
                http_client=proxy_client
                )

from app import routes, models