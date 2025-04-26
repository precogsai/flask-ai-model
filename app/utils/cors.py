from flask_cors import CORS

def configure_cors(app):
    """
    Configure CORS for the Flask app.

    Allows specific origins, methods, and headers for security.
    """
    cors = CORS(
        app,
        resources={
            r"/*": {
                "origins": ["http://localhost:3000", "https://your-production-domain.com"],  # Allowed Frontend URLs
                "methods": ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
                "allow_headers": ["Content-Type", "Authorization"],
                "supports_credentials": True
            }
        }
    )
    return cors
