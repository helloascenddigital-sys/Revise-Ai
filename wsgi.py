"""WSGI entry point for Gunicorn (used on Render.com)"""

import os
from backend.app import app

if __name__ == "__main__":
    app.run()
