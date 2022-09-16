from flask import Flask

from lesson23_project_source.views import app_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(app_bp)

    return app

