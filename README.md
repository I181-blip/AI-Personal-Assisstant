# AI Personal Assistant

A command-line AI assistant built in Python that uses Google's Gemini API to understand natural language and reply conversationally. Built as Project 01 of the HexSoftwares AI internship.

## Features

- Chat with an LLM directly in the terminal
- Answers questions, explains concepts, and summarizes text you paste in
- Loads the API key securely from a `.env` file
- Handles errors (rate limits, network issues) without crashing
- Type `exit` or `quit` to stop

## Tech Stack

- Python 3
- Google Gemini API (`google-genai`)
- `python-dotenv`

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/AI-Personal-Assistant.git
   cd AI-Personal-Assistant
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   python -m pip install -r requirements.txt
   ```

4. **Add your API key.** Get a free key from [Google AI Studio](https://aistudio.google.com), then create a file named `.env` in the project folder:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

5. **Run the assistant**
   ```bash
   python app.py
   ```

## Example

```
AI Assistant ready. Type 'exit' to quit.
You: hello
Assistant: Hello! How can I help you today?
You: Explain machine learning in 2 lines
Assistant: Machine learning is a branch of AI where computers learn from data...
```

## Notes

- The free Gemini tier has request limits (about 5 requests per minute on some models). If you see a 429 or 503 error, wait a few seconds and try again.
- If a model name stops working, update the `model=` value in `app.py` to a currently available Gemini model.
- Never upload your `.env` file. It is listed in `.gitignore`.

## Future Improvements

- Save answers as Word documents
- Add conversation memory for multi-turn context
- Add reminders and scheduling

