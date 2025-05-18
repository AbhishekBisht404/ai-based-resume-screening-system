import re
# import pandas as pd
# import spacy
#
# nlp = spacy.load('en_core_web_lg')
# df = pd.read_csv('resumes.csv')
#
def categorize_job_title_with_regex(job_title):
    job_title_lower = str(job_title).lower()
    if re.search(r'\b(web|frontend|front[- ]?end|backend|back[- ]?end|full[- ]?stack)\b', job_title_lower):
        return 'Web Developer'
    elif re.search(r'\b(software|engineer|developer|programmer)\b', job_title_lower):
        return 'Software Engineer'
    elif re.search(r'\b(data\s*scientist|data\s*analyst|ml|ai|machine\s*learning|deep\s*learning)\b', job_title_lower):
        return 'Data Scientist'
    elif re.search(r'\b(cyber|security|information\s*security)\b', job_title_lower):
        return 'Cyber Security'
    elif re.search(r'\b(devops|cloud|aws|azure|gcp|infrastructure|ci/cd|docker|kubernetes)\b', job_title_lower):
        return 'DevOps / Cloud Engineer'
    else:
        return 'Other'

# def clean_resume(resume_text):
#     resume_text = str(resume_text).lower()
#     resume_text = re.sub(r'[^a-zA-Z\s]', ' ', resume_text)
#     resume_text = re.sub(r'\s+', ' ', resume_text).strip()
#     doc = nlp(resume_text)
#     cleaned_tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
#     return ' '.join(cleaned_tokens)
#
# df['cleaned_resume'] = df['resume'].apply(clean_resume)
#
# df['job_category'] = df['job_title'].apply(categorize_job_title_with_regex)
#
# # Filter only relevant categories
# df_cleaned = df[df['job_category'] != 'Other'].copy()
# df_cleaned.to_csv('cleaned_resumes.csv', index=False)
# print("Cleaned resume saved!")