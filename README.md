# ChatBot

A modern chatbot web app using Google Gemini API and Streamlit.

## Features
- Chat with Gemini LLM using your API key
- Modern chat UI with bubbles and fixed input bar
- Easy to deploy and run locally

## Setup Instructions

### 1. Clone the repository

git clone https://github.com/Balkrishna7461/ChatBot.git


### 2. Create and activate a virtual environment (optional but recommended)

python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate


### 3. Install dependencies

pip install -r requirements.txt


### 4. Set up your Gemini API key
- Create a `.env` file in the `ChatBot-1` directory with this content:
  ```env
  GEMINI_API_KEY=your_gemini_api_key_here
  ```

### 5. Run the chatbot
```bash
streamlit run gemini_chatbot.py
```

### 6. Open in your browser
- The app will open automatically, or visit: [http://localhost:8501](http://localhost:8501)

## Deployment
You can deploy this app to any platform that supports Python and Streamlit (e.g., Streamlit Community Cloud, Heroku, etc.).

## License
MIT