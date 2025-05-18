import re
from typing import Dict, List
import spacy

nlp = spacy.load("en_core_web_lg")

EDUCATION_KEYWORDS = [
    'bachelor', 'master', 'b.tech', 'm.tech', 'b.sc', 'm.sc',
    'b.e', 'm.e', 'phd', 'mba', 'bca', 'mca', 'high school'
]

EXPERIENCE_KEYWORDS = ['experience', 'worked', 'internship', 'employment', 'responsibilities']

LABEL_LINES = ['email', 'phone', 'name', 'location', 'education']

def clean_text(text: str) -> str:
    lines = text.split('\n')
    cleaned_lines = [
        line for line in lines
        if not re.match(r'^\s*(' + '|'.join(LABEL_LINES) + r')\s*$', line.strip().lower())
    ]
    return '\n'.join(cleaned_lines)

def extract_email(text: str) -> str:
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group(0) if match else None

def extract_phone(text: str) -> str:
    match = re.search(r'(\+?\d{1,3})?[\s\-\.]?\(?\d{3}\)?[\s\-\.]?\d{3}[\s\-\.]?\d{4}', text)
    return match.group(0) if match else None

def extract_name(text: str) -> str:
    first_line = text.split('\n')[0]
    doc = nlp(first_line)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ' '.join(ent.text.split()).strip()
    return None

def extract_education(text: str) -> List[str]:
    lines = text.split('\n')
    found = []
    for line in lines:
        line_lower = line.strip().lower()
        if line_lower in LABEL_LINES:
            continue  # skip label-only lines
        for keyword in EDUCATION_KEYWORDS:
            if keyword in line_lower:
                found.append(line.strip())
                break
    return list(set(found))

def extract_experience(text: str) -> List[str]:
    lines = text.split('\n')
    exp_sections = []
    for line in lines:
        line_lower = line.lower().strip()
        if line_lower in LABEL_LINES:
            continue  # skip label-only lines
        if any(word in line_lower for word in EXPERIENCE_KEYWORDS):
            exp_sections.append(line.strip())
    return exp_sections

def parse_resume(text: str) -> Dict:
    cleaned_text = clean_text(text)
    return {
        "name": extract_name(cleaned_text),
        "email": extract_email(cleaned_text),
        "phone": extract_phone(cleaned_text),
        "education": extract_education(cleaned_text),
        "experience_summary": extract_experience(cleaned_text)
    }

#
# Example usage:
# if __name__ == "__main__":
#     sample_resume = """
#     Name: John Doe
#     Email: john.doe@gmail.com
#     Phone: +1 (555) 123-4567 ext 101
#     Location: San Francisco
#     Education
#     Bachelor of Technology in Computer Science from XYZ University.
#     Experienced Software Engineer with 3 years at Google.
#     Worked on backend microservices and infrastructure.
#     Internship at ABC Corp from June 2018 to August 2018.
#     """
#     parsed = parse_resume(sample_resume)
#     for k, v in parsed.items():
#         print(f"{k.capitalize()}: {v}")
