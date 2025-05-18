from typing import List, Dict
import spacy

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

ner_model = spacy.load('models/custom_ner_model')

def extract_skills_with_ner(text: str) -> List[str]:
    doc = ner_model(text)
    skills = [ent.text.lower() for ent in doc.ents if ent.label_.lower() == "skill"]
    return list(set(skills))

def weighted_keyword_score(text: str, kws_weights: Dict[str, int]) -> int:
    text = text.lower()
    return sum(weight for kw, weight in kws_weights.items() if kw in text)

def score_resume(texts: List[str], predicted_categories: List[str], extracted_skills: List[List[str]]) -> List[Dict]:
    reports = []

    for i in range(len(texts)):
        text = texts[i].lower()
        pred_cat = predicted_categories[i]
        skills = set(skill.lower() for skill in extracted_skills[i])

        keyword_score = weighted_keyword_score(text, WEIGHTED_KEYWORDS.get(pred_cat, {}))
        keyword_score_norm = min(keyword_score / 10, 1.0)  # normalize to max 10 points

        expected_skills = set(WEIGHTED_KEYWORDS.get(pred_cat, {}).keys())
        matched_skills = expected_skills.intersection(skills)
        skill_score = len(matched_skills) / len(expected_skills) if expected_skills else 0

        final_score = round((0.6 * keyword_score_norm + 0.4 * skill_score) * 10, 2)

        missing_skills = expected_skills - skills

        report = {
            'predicted_category': pred_cat,
            'keyword_score': round(keyword_score_norm * 10, 2),
            'skill_match_score': round(skill_score * 10, 2),
            'final_resume_score': final_score,
            'matched_skills': list(matched_skills),
            'missing_skills': missing_skills
        }

        reports.append(report)

    return reports

# # --- Test block ---
# if __name__ == "__main__":
#     sample_resumes = [
#         "Frontend developer experienced in HTML, CSS, JavaScript, and React. Built several SPAs.",
#         "Cybersecurity engineer skilled in penetration testing and threat detection. Familiar with firewalls and SIEM.",
#         "Software engineer working with Java, unit testing, and microservices.",
#         "Data scientist proficient in machine learning, deep learning, pandas, and data visualization.",
#         "DevOps engineer with hands-on experience in Docker, Kubernetes, CI/CD pipelines, and AWS infrastructure."
#     ]
#
#     predicted_categories = [
#         'web_developer',
#         'cybersecurity',
#         'software_engineer',
#         'data_scientist',
#         'devops_cloud_engineer'
#     ]
#
#     # Extract skills using NER model
#     extracted_skills = [extract_skills_with_ner(resume) for resume in sample_resumes]
#
#     scores = score_resume(sample_resumes, predicted_categories, extracted_skills)
#
#     for i, report in enumerate(scores):
#         print(f"\nResume {i+1} ({predicted_categories[i]}):")
#         for k, v in report.items():
#             print(f"  {k.replace('_', ' ').capitalize()}: {v}")
#
#     print("\n--- NER Debug ---")
#     for i, resume in enumerate(sample_resumes):
#         doc = ner_model(resume)
#         print(f"Resume {i+1} Entities:", [(ent.text, ent.label_) for ent in doc.ents])
