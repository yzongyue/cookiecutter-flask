# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
import importlib
import os

from flask import Flask, render_template, Blueprint
from werkzeug.utils import find_modules

from {{cookiecutter.app_name}}.settings import ProdConfig
from {{cookiecutter.app_name}}.assets import assets
from {{cookiecutter.app_name}}.extensions import (
    bcrypt,
    cache,
    db,
    login_manager,
    mail,
    migrate,
    debug_toolbar,
)


def create_app(config_object=ProdConfig):
    """An application factory, as explained here:
        http://flask.pocoo.org/docs/patterns/appfactories/

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__)
    app.config.from_object(config_object)

    if config_object == ProdConfig:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

    register_extensions(app)
    top_mod = __name__.split('.')[0]
    register_blueprints(app, top_mod + '.views')
    register_errorhandlers(app)
    return app

def register_extensions(app):
    assets.init_app(app)
    bcrypt.init_app(app)
    cache.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    debug_toolbar.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    return None


def register_blueprints(app, import_path, bp_name='blueprint'):
    for name in find_modules(import_path, include_packages=True):
        mod = importlib.import_module(name)
        bp = getattr(mod, bp_name, None)
        if isinstance(bp, Blueprint):
            app.register_blueprint(bp)
    return None


def register_errorhandlers(app):
    def render_error(error):
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, 'code', 500)
        return render_template("{0}.html".format(error_code)), error_code
    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None
