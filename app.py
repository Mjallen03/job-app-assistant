from flask import Flask, render_template, request
from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        job_description = request.form.get("job_description")
        resume = request.form.get("resume")

        prompt = f"""You are a career coach helping someone tailor their resume for a job application.

JOB DESCRIPTION:
{job_description}

RESUME:
{resume}

Provide:
1. A match score out of 100
2. Top 5 keywords from the job description missing from the resume
3. 3 specific resume bullet point suggestions to better align with this job
4. 3 likely interview questions based on this job description

Format your response clearly with headers for each section."""

        message = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}]
        )
        result = message.content[0].text

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)