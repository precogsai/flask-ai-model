import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import yaml

from app.routes import home, health, scan
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

    # ✅ API Token for protecting routes
    API_TOKEN = os.getenv("API_TOKEN", "default-secret-token")

    @app.before_request
    def verify_api_token():
        # Allow public routes like /health and home(/) without token
        if request.path not in ["/", "/health"]:
            token = request.headers.get("Authorization")
            if token != f"Bearer {API_TOKEN}":
                return jsonify({"error": "Unauthorized"}), 401
        return None

        

    # Register blueprints
    app.register_blueprint(home.bp)
    app.register_blueprint(health.bp)
    app.register_blueprint(scan.bp)

    return app
