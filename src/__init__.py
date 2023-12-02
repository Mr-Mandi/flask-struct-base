from flask import Flask

# Routes

app = Flask(__name__)


def init_app(config):
    # Configuration
    app.config.from_object(config)

    # Blueprints
    #app.register_blueprint("cal", url_prefix='/')


    return app