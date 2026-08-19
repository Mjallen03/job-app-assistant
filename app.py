from flask import Flask, render_template, request
from anthropic import Anthropic
from dotenv import load_dotenv
from werkzeug.utils import secure_filename
import os
import tempfile
import pdfplumber
import docx

load_dotenv()

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def extract_text_from_file(file):
    filename = file.filename.lower()
    file_bytes = file.read()
    print(f"DEBUG: filename={filename}, bytes={len(file_bytes)}")

    try:
        if filename.endswith('.pdf'):
            with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp:
                tmp.write(file_bytes)
                tmp_path = tmp.name
            with pdfplumber.open(tmp_path) as pdf:
                text = "".join(page.extract_text() or "" for page in pdf.pages)
            os.unlink(tmp_path)
            print(f"DEBUG: PDF text length={len(text)}")
            return text if text.strip() else None

        elif filename.endswith('.docx'):
            with tempfile.NamedTemporaryFile(delete=False, suffix='.docx') as tmp:
                tmp.write(file_bytes)
                tmp_path = tmp.name
            doc = docx.Document(tmp_path)
            text = "\n".join(para.text for para in doc.paragraphs)
            os.unlink(tmp_path)
            print(f"DEBUG: DOCX text length={len(text)}")
            return text if text.strip() else None

        elif filename.endswith('.txt'):
            return file_bytes.decode('utf-8')

    except Exception as e:
        print(f"DEBUG: Error={e}")
        return None

    return None

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        print(f"DEBUG: files={request.files}")
        print(f"DEBUG: form keys={list(request.form.keys())}")

        job_description = request.form.get("job_description")
        resume_text = request.form.get("resume")
        resume_file = request.files.get("resume_file")

        print(f"DEBUG: resume_file={resume_file}, filename={resume_file.filename if resume_file else 'NONE'}")

        if resume_file and resume_file.filename:
            extracted = extract_text_from_file(resume_file)
            if extracted:
                resume_text = extracted
            else:
                error = "Could not extract text from your file. Try pasting your resume instead."

        if not error and job_description and resume_text:
            prompt = f"""You are a career coach helping someone tailor their resume for a job application.

JOB DESCRIPTION:
{job_description}

RESUME:
{resume_text}

Provide:
1. A match score out of 100
2. Top 5 keywords from the job description missing from the resume
3. 3 specific resume bullet point suggestions to better align with this job
4. 3 likely interview questions based on this job description

Format your response clearly with headers for each section."""

            message = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=2048,
                messages=[{"role": "user", "content": prompt}]
            )
            result = message.content[0].text

    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)