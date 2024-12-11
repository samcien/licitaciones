from flask import Flask
from flask_mysql import MySQL

mysql = MySQL()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    mysql.init_app(app)

    from .routes import api_bp
    app.register_blueprint(api_bp)

    return app
