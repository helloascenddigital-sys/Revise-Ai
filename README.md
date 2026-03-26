# Revised AI - AI-Powered Study Assistant

An intelligent study assistant that helps students understand complex topics through AI-powered explanations. Built with Streamlit frontend and Flask backend, powered by DeepSeek AI via SambaNova.

## Features

✅ **Instant Explanations** - Get detailed explanations of any academic topic
✅ **Clean UI** - Modern, intuitive interface with conversation history
✅ **Response Caching** - Fast retrieval of previously asked topics
✅ **Free to Deploy** - Runs on Render (backend) + Streamlit Cloud (frontend)

## Tech Stack

- **Frontend**: Streamlit 1.22.0
- **Backend**: Flask 2.0.3 + Gunicorn
- **AI Model**: DeepSeek-R1-0528 via SambaNova API
- **Deployment**: Render.com (backend) + Streamlit Cloud (frontend)

## Project Structure

```
revised-ai/
├── backend/                 # Flask API server
│   ├── app.py              # Main Flask app & /explain endpoint
│   ├── models/             # AI model interfaces
│   │   └── gemini.py       # DeepSeek/SambaNova integration
│   ├── utils/              # Utilities
│   │   └── cache.py        # Response caching
│   └── requirements.txt     # Backend dependencies
├── frontend/               # Streamlit UI
│   ├── app.py              # Main Streamlit app
│   ├── styles.css          # Custom styling
│   └── requirements.txt     # Frontend dependencies
├── .streamlit/             # Streamlit Cloud config
│   └── config.toml         # Streamlit settings
├── wsgi.py                 # WSGI entry point for Gunicorn
├── Procfile                # Render deployment config
├── requirements.txt        # Root dependencies
├── DEPLOY_STEPS.md         # Detailed deployment guide
└── README.md               # This file
```

## Quick Start (Local Development)

### Prerequisites
- Python 3.8+
- SambaNova API key ([get here](https://cloud.sambanova.com))

### Setup

1. **Clone and navigate:**
   ```bash
   git clone https://github.com/yourusername/revised-ai.git
   cd revised-ai
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment:**
   ```bash
   # Create .env file
   echo SAMBANOVA_API_KEY=your_key_here > .env
   echo CACHE_EXPIRATION=3600 >> .env
   ```

5. **Run the application:**
   ```bash
   python -m backend.app
   ```

2. Start the Streamlit frontend:

   ```
   streamlit run frontend/app.py
   ```

3. Open your web browser and navigate to `http://localhost:8501`

## Usage Guide

1. **Select Mode**:

   - Choose "Explain a Topic" to get explanations
   - Choose "Summarize Text" to summarize content

2. **Input Content**:

   - For explanations, enter a topic you want to learn about
   - For summaries, paste the text you want to summarize

3. **Submit**:
   - Click the "Submit" button to process your request
   - View the AI-generated response in the chat interface

## Project Structure

```
revise_ai/
├── .env                  # Environment variables (API keys)
├── backend/
│   ├── __init__.py
│   ├── app.py            # Flask application
│   ├── models/
│   │   └── gemini.py     # Gemini API integration
│   └── utils/
│       └── cache.py      # Caching mechanism
├── frontend/
│   └── app.py            # Streamlit application
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
