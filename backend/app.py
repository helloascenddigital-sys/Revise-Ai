from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json
from dotenv import load_dotenv
from .models.gemini import DeepSeekAPI
from .utils.cache import Cache

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for Streamlit frontend

# Initialize DeepSeek API and cache
cache = Cache(expiration=int(os.getenv("CACHE_EXPIRATION", "3600").split()[0]))


@app.route("/", methods=["GET"])
def index():
    """Basic route for Render health checks and quick verification."""
    return jsonify({"status": "ok", "service": "revised-ai-api"}), 200


@app.route("/health", methods=["GET"])
def health():
    """Explicit health check endpoint."""
    return jsonify({"status": "healthy"}), 200


@app.route("/explain", methods=["POST"])
def explain():
    """Endpoint for generating explanations of topics"""
    data = request.json
    topic = data.get("topic")

    if not topic:
        return jsonify({"error": "No topic provided"}), 400

    # Check cache first
    cache_key = f"explain_{topic}"
    cached_response = cache.get(cache_key)

    if cached_response:
        return jsonify({"explanation": cached_response})

    try:
        explanation = DeepSeekAPI(
            api_key=os.getenv("SAMBANOVA_API_KEY")
        ).generate_explanation(topic)
        # Cache the response
        cache.set(cache_key, explanation)
        return jsonify({"explanation": explanation})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)
