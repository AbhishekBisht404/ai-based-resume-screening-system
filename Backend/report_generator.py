from typing import List, Dict
import spacy
import re
from job_role_predictor import ensemble_predict
from suggestions_generator import generate_suggestions
from scoring_resume import score_resume as scoring_score_resume

ner_model = spacy.load('models/custom_ner_model')

VALID_SKILLS = {
    'python', 'java', 'c++', 'machine learning', 'deep learning', 'docker', 'kubernetes',
    'react', 'javascript', 'aws', 'azure', 'html', 'css', 'sql', 'tensorflow', 'pandas',
    'microservices', 'unit testing', 'ci/cd', 'backend', 'frontend', 'software engineer',
    'data science', 'penetration testing', 'threat detection', 'cloud', 'devops'
}

WEIGHTED_KEYWORDS = {
    'software_engineer': {
        'software engineer': 3, 'backend': 2, 'unit testing': 2, 'java': 2, 'microservices': 2
    },
    'web_developer': {
        'frontend': 3, 'html': 2, 'css': 2, 'javascript': 2, 'react': 2
    },
    'data_scientist': {
        'data science': 3, 'machine learning': 3, 'deep learning': 2, 'pandas': 1, 'statistics': 1
    },
    'cybersecurity': {
        'cybersecurity': 3, 'penetration testing': 3, 'threat detection': 2, 'vulnerability': 1
    },
    'devops_cloud_engineer': {
        'docker': 2, 'kubernetes': 2, 'aws': 2, 'devops': 3, 'ci/cd': 2
    }
}

def to_title_case_preserve_acronyms(text: str) -> str:
    return ' '.join(word if word.isupper() else word.capitalize() for word in text.split())


def extract_skills_with_ner(text: str) -> List[str]:
    title_case_text = to_title_case_preserve_acronyms(text)
    doc = ner_model(title_case_text)

    ner_skills = {ent.text.lower() for ent in doc.ents if ent.label_.lower() == "skill"}

    fallback_skills = {skill for skill in VALID_SKILLS if skill in text.lower()}

    return sorted(ner_skills.union(fallback_skills))

def score_resume(texts: List[str], extracted_skills: List[List[str]]) -> List[Dict]:
    predicted_categories = [ensemble_predict(text).strip().lower().replace(' ', '_') for text in texts]
    reports = scoring_score_resume(texts, predicted_categories, extracted_skills)

    for report in reports:
        missing_skills = report.get('missing_skills', [])
        report['skill_suggestions'] = generate_suggestions(missing_skills)
        report['predicted_category'] = report['predicted_category'].replace('_', ' ').title()

    return reports

# if __name__ == "__main__":
#     sample_resumes = [
#         "Frontend developer experienced in HTML, CSS, JavaScript, and React. Built several SPAs.",
#         "Cybersecurity engineer skilled in Penetration Testing and Threat Detection. Familiar with Firewalls and SIEM.",
#         "Software engineer working with Java, Unit testing, and Microservices.",
#         "Data scientist proficient in Machine Learning, Deep Learning, Pandas, and Data Visualization.",
#         "DevOps engineer with hands-on experience in Docker, Kubernetes, CI/CD pipelines, and AWS infrastructure."
#     ]
#
#     raw_skills = [extract_skills_with_ner(text) for text in sample_resumes]
#     scores = score_resume(sample_resumes, raw_skills)
#
#     for i, report in enumerate(scores):
#         print(f"\nResume {i + 1}: {sample_resumes[i][:50]}...")
#         for k, v in report.items():
#             print(f"  {k.replace('_', ' ').capitalize()}: {v}")
