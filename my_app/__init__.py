from flask import Flask
from my_app.models import setup_db, db_drop_and_create_all
from flask_cors import CORS
import os
from dotenv import load_dotenv




app = Flask(__name__)
setup_db(app)
CORS(app)
load_dotenv()

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['SECRET_KEY'] = "ad58a088892dd3940eb141ebf15bd822c957e3aa91ce93c9b28c65da7a1f0c5b"
# db = SQLAlchemy(app)

# with app.app_context(): 
#     db_drop_and_create_all()

from my_app import routes