# Job Application Assistant

A web app that analyzes how well your resume matches a job description using Claude AI. Get a match score, see missing keywords, get tailored resume bullet point suggestions, and prep with likely interview questions — all in seconds.

## Why I built this

As a recent Software Engineering graduate applying to roles, I wanted a way to quickly understand how well my resume aligned with specific job postings before submitting — and to learn how to build real applications on top of AI APIs in the process.

## Features

- Paste any job description and resume to get an instant match score (0-100)
- Identifies top missing keywords from the job posting
- Suggests specific resume bullet point rewrites
- Generates likely interview questions based on the role

## Tech Stack

- **Backend:** Python, Flask
- **AI:** Anthropic Claude API
- **Frontend:** HTML, CSS
- **Environment management:** python-dotenv

## How It Works

1. User submits a job description and their resume through a simple web form
2. The Flask backend sends both to Claude with a structured prompt
3. Claude analyzes the alignment and returns a formatted breakdown
4. Results are displayed directly in the browser

## Running Locally

```bash
git clone https://github.com/Mjallen03/job-app-assistant.git
cd job-app-assistant
python -m venv venv
venv\Scripts\activate
pip install flask anthropic python-dotenv
```

Create a `.env` file in the root directory with your Anthropic API key:


Then run:

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

## What I'd Add Next

- Deploy publicly so it's accessible without running locally
- Save analysis history
- Support PDF resume uploads instead of pasted text
- Add a cover letter generator

## About Me

Built by Marcus Allen, Software Engineering graduate (WGU). Connect with me on [LinkedIn](https://www.linkedin.com/in/marcus-allen-503257137/) or check out my other projects on [GitHub](https://github.com/Mjallen03).