from flask import Flask, render_template
from app.routes import user_routes
from app.routes import dash

def create_app():

    app = Flask(__name__)
    app.register_blueprint(user_routes.bp)
    app.register_blueprint(dash.bp)


    return app