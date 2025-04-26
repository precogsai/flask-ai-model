import os
from flask import Flask
from dotenv import load_dotenv
import yaml

from app.routes import home, health
from app.config.config import Config
from app.utils.cors import configure_cors  # ✅ Import your clean CORS function

def create_app():
    # Load environment variables from .env
    load_dotenv()

    # Create Flask app
    app = Flask(__name__)

    # Load default configurations
    app.config.from_object(Config)

    # Load additional YAML configurations if exists
    if os.path.exists('config.yaml'):
        with open('config.yaml') as f:
            yaml_config = yaml.safe_load(f)
            app.config.update(yaml_config)

    # Setup CORS policy cleanly
    configure_cors(app)

    # Register blueprints
    app.register_blueprint(home.bp)
    app.register_blueprint(health.bp)

    return app
