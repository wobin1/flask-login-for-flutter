from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'something only you know'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cnmaanlbnytyje:ed87fcfe28d3ac14fd4fc8ffce12bc1540e036af08581184450ddd1f0a2478ef@ec2-18-210-233-138.compute-1.amazonaws.com:5432/d6d2sieslt4udv'
    app.config['SQLALCHEM_TRACK_MODIFICATION'] = False

    db.init_app(app)

    from .views import views

    app.register_blueprint(views)

    return app