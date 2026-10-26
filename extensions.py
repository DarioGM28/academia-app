
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Inicialización de SQLAlchemy
db = SQLAlchemy()

# Inicialización de Flask-Migrate
migrate = Migrate()
