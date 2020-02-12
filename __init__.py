import os
from flask import Flask, redirect, url_for

def not_found(e):
    return redirect(url_for('auth.login')), 404

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.register_error_handler(404, not_found)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'youtube.sqlite')
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from youtube.db import get_db

    db.init_app(app)

    from youtube import auth
    from youtube import sla

    app.register_blueprint(auth.bp)
    app.register_blueprint(sla.bp)

    return app