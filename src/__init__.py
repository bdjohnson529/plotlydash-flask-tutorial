"""Initialize Flask app."""
from flask import Flask
from flask_assets import Environment

# Import Dash application
from .homepage import init_app as init_homepage
from .tablepage import init_app as init_inputpage1
from .formpage import init_app as init_inputpage2
from .plotlydash.dashboard1 import init_app as init_dashboard1
from .plotlydash.dashboard2 import init_app as init_dashboard2
from .plotlydash.dashboard3 import init_app as init_dashboard3
from .assets import compile_static_assets


def init_app():
    """Construct core Flask application with embedded Dash app."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    assets = Environment()
    assets.init_app(app)

    with app.app_context():
        # Initialize pages
        app = init_homepage(app)
        app = init_inputpage1(app)
        app = init_inputpage2(app)
        app = init_dashboard1(app)
        app = init_dashboard2(app)
        app = init_dashboard3(app)

        # Compile static assets
        compile_static_assets(assets)



        return app
