# Job Application Assistant

A web app that analyzes how well your resume matches a job description using Claude AI. Get a match score, see missing keywords, get tailored resume bullet point suggestions, and prep with likely interview questions — all in seconds.

🔗 **Live Demo:** [job-app-assistant-nmd6.onrender.com](https://job-app-assistant-nmd6.onrender.com)

## Why I built this

As a recent Software Engineering graduate applying to roles, I wanted a way to quickly understand how well my resume aligned with specific job postings before submitting — and to learn how to build real applications on top of AI APIs in the process.

## Features

- Upload your resume as a PDF, Word doc, or .txt file — or paste it as text
- Paste any job description to get an instant match score (0-100)
- Identifies top missing keywords from the job posting
- Suggests specific resume bullet point rewrites
- Generates likely interview questions based on the role

## Tech Stack

- **Backend:** Python, Flask
- **AI:** Anthropic Claude API
- **Frontend:** HTML, CSS
- **File parsing:** pdfplumber, python-docx
- **Environment management:** python-dotenv

## How It Works

1. User uploads or pastes their resume and pastes a job description
2. The Flask backend extracts text from the file if uploaded
3. Both are sent to Claude with a structured prompt
4. Claude analyzes the alignment and returns a formatted breakdown
5. Results are displayed directly in the browser

## Running Locally

Clone the repo, install dependencies, add your API key, and run:

```bash
git clone https://github.com/Mjallen03/job-app-assistant.git
cd job-app-assistant
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
echo ANTHROPIC_API_KEY=your_key_here > .env
python app.py
```

Replace `your_key_here` with your actual [Anthropic API key](https://console.anthropic.com). Then visit `http://127.0.0.1:5000` in your browser.

## What I'd Add Next

- Save analysis history
- Cover letter generator based on job description
- Better formatted output with styled sections
- Job application tracker

## About Me

Built by Marcus Allen, Software Engineering graduate (WGU). Connect with me on [LinkedIn](https://www.linkedin.com/in/marcus-allen-503257137/) or check out my other projects on [GitHub](https://github.com/Mjallen03).