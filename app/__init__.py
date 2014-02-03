from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate

app = Flask(__name__)
app.config['SLQALCHEMY_DATABASE_URI'] = 'your-sql-alchemy-db-uri'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)

from app import views
from app import models

if __name__ == '__main__':
    app.run()
