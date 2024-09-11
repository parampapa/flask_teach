from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

migrate = Migrate()
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()