import os
from flask import Flask
from config import DevConfig, ProdConfig, TestConfig
def create_app(config_type=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path, 'src.sqlite')
    )
    
    if config_type is None:
        app.config.from_object(DevConfig)
    if config_type == 'Prod':
        app.config.from_object(ProdConfig)
    if config_type == 'test':
        app.config.from_object(TestConfig)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        app.log_exception(OSError)
    
    from . import db
    db.init_app(app)
    from . import auth
    app.register_blueprint(auth.bp)

    return app