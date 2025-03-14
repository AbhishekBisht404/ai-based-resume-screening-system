import joblib
from fastapi import FastAPI, UploadFile, File, Form
import pdfplumber
import docx2txt
import re
from fastapi.middleware.cors import CORSMiddleware


# Load trained ML model and vectorizer
model = joblib.load("resume_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")
label_encoder = joblib.load("label_encoder.pkl")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (change this in production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Job skills dictionary
JOB_SKILLS = {
    "Software Engineer": {"python", "java", "c++", "data structures", "algorithms", "git"},
    "Web Developer": {"html", "css", "javascript", "react", "node.js", "express", "mongodb"},
    "Data Scientist": {"python", "machine learning", "deep learning", "sql", "pandas", "numpy"},
    "DevOps Engineer": {"docker", "kubernetes", "aws", "linux", "jenkins", "terraform"},
    "Cybersecurity Analyst": {"network security", "penetration testing", "cryptography", "linux"},
    "UI/UX Designer": {"figma", "adobe xd", "user research", "wireframing"},
}


# Function to extract text from PDF/DOCX
def extract_text_from_resume(file):
    if file.filename.endswith(".pdf"):
        with pdfplumber.open(file.file) as pdf:
            return " ".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    elif file.filename.endswith(".docx"):
        return docx2txt.process(file.file)
    else:
        return ""


# Function to extract skills from text
def extract_skills(text):
    text = text.lower()
    skills_found = set()
    for job, skills in JOB_SKILLS.items():
        for skill in skills:
            if re.search(rf"\b{skill}\b", text):
                skills_found.add(skill)
    return skills_found


# API Endpoint for Resume Scoring
@app.post("/analyze_resume/")
async def analyze_resume(file: UploadFile = File(...), job_role: str = Form(...)):
    try:
        # Extract text from resume
        resume_text = extract_text_from_resume(file)

        if not resume_text:
            return {"error": "Unable to extract text from the resume."}

        # Transform text and predict job role
        transformed_text = vectorizer.transform([resume_text])
        prediction = model.predict(transformed_text)
        predicted_category = label_encoder.inverse_transform(prediction)[0]

        # Extract skills
        extracted_skills = extract_skills(resume_text)

        # Get required skills for selected job role
        job_role = job_role.strip()
        required_skills = JOB_SKILLS.get(job_role, set())

        # Calculate missing skills
        # Calculate missing skills
        missing_skills = required_skills - extracted_skills
        missing_skills_list = list(missing_skills) if missing_skills else [
            "No missing skills. You have all the required skills! 🎯"]

        # Calculate resume score
        resume_score = (len(extracted_skills.intersection(required_skills)) / len(required_skills)) * 100 if required_skills else 0

        # Generate recommendations
        if resume_score == 100:
            suggestions = "Your resume is well-matched for this job role!"
        elif resume_score >= 70:
            suggestions = "Your resume is strong, but consider learning: " + ", ".join(missing_skills)
        else:
            suggestions = "Your resume needs improvement. Learn these skills: " + ", ".join(missing_skills)

        return {
            "Predicted Job Role": predicted_category,
            "Selected Job Role": job_role,
            "Resume Score": round(resume_score, 2),
            "Extracted Skills": list(extracted_skills),
            "Missing Skills": missing_skills_list,
            "Suggestions": suggestions
        }

    except Exception as e:
        return {"error": str(e)}
