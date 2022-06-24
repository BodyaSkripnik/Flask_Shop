from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ferfrefergegegegregergreg4t3rfger'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_BASE')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

UPLOAD_FOLDER = 'static/img/uploads/'#для загрузки фото
  
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER#для загрузки фото
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024#для загрузки фото
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])#для загрузки фото
def allowed_file(filename):#для загрузки фото
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS#для загрузки фото

  
db = SQLAlchemy(app)
migrate = Migrate(app,db)
login_manager = LoginManager(app)
login_manager.login_view = 'login_page'
login_manager.login_message = 'Авторизуйтесь для доступу до сторінки'
login_manager.login_message_category = 'success'
from models import *