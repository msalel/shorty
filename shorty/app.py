from flask import Flask
from shorty.api import api
from shorty.errors import errors
from dotenv import load_dotenv


def create_app(settings_overrides=None):
    app = Flask(__name__)
    load_dotenv()
    configure_settings(app, settings_overrides)
    configure_blueprints(app)
    return app


def configure_settings(app, settings_override):
    app.config.update({
        'DEBUG': True,
        'TESTING': False,
    })
    if settings_override:
        app.config.update(settings_override)


def configure_blueprints(app):
    app.register_blueprint(api)
    app.register_blueprint(errors)