from fastapi import FastAPI, HTTPException, UploadFile, File
from custom_parser import parse_resume
from report_generator import extract_skills_with_ner, score_resume
from fastapi.middleware.cors import CORSMiddleware
import fitz
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def extract_text_with_pymupdf(file: UploadFile) -> str:
    text = ""
    with open("temp.pdf", "wb") as f:
        f.write(file.file.read())

    doc = fitz.open("temp.pdf")
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

@app.post("/api/analyze_resumes")
async def analyze_resumes(resume: UploadFile = File(...)):
    text = extract_text_with_pymupdf(resume)

    extracted_skills = extract_skills_with_ner(text)

    report = score_resume([text], [extracted_skills])[0]

    parsed_info = parse_resume(text)

    return {
        "results": [
            {
                "parsed_info": parsed_info,
                "score_report": report
            }
        ]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
