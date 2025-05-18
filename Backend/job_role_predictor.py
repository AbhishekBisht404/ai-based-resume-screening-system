import joblib
import pandas as pd
from scipy.sparse import hstack, csr_matrix
from collections import Counter
import warnings
vectorizer = joblib.load('models/tfidf_vectorizer.pkl')
label_encoder = joblib.load('models/label_encoder.pkl')

model_files = ['models/logistic_regression.pkl', 'models/lightgbm.pkl', 'models/random_forest.pkl', 'models/xgboost.pkl']
ml_models = [joblib.load(f) for f in model_files]


weighted_keywords = {
    'software_engineer': {
        'software engineer': 3,
        'object-oriented programming': 2,
        'design patterns': 2,
        'multithreading': 1
    },
    'web_developer': {
        'frontend developer': 3,
        'responsive design': 2,
        'react': 1,
        'javascript': 1,
        'html': 1,
        'css': 1,
        'node.js': 1,
        'webpack': 1
    },
    'devops_cloud_engineer': {
        'devops': 3,
        'kubernetes': 2,
        'docker': 1,
        'aws': 1,
        'jenkins': 1,
        'infrastructure as code': 2,
        'serverless architecture': 2
    },
    'cybersecurity': {
        'cybersecurity': 3,
        'penetration testing': 2,
        'threat detection': 1,
        'wireshark': 1,
        'metasploit': 1,
        'nessus': 1,
        'siem': 1
    },
    'data_scientist': {
        'machine learning': 3,
        'data analysis': 2,
        'deep learning': 1,
        'tensorflow': 1,
        'pytorch': 1,
        'pandas': 1,
        'numpy': 1,
        'feature engineering': 2
    }
}

def weighted_keyword_score(text, kws_weights):
    text = text.lower()
    score = 0
    for kw, weight in kws_weights.items():
        if kw in text:
            score += weight
    return score

def extract_weighted_features(text, weighted_kws_dict):
    features = {}
    for category, kws_weights in weighted_kws_dict.items():
        features[category] = weighted_keyword_score(text, kws_weights)
    return pd.DataFrame([features])

def ensemble_predict(text: str) -> str:
    tfidf_vector = vectorizer.transform([text])
    kw_df = extract_weighted_features(text, weighted_keywords)
    kw_sparse = csr_matrix(kw_df.values)
    combined_input = hstack([tfidf_vector, kw_sparse])

    preds = []
    for model in ml_models:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            pred_num = model.predict(combined_input)[0]
        pred_label = label_encoder.inverse_transform([pred_num])[0]
        preds.append(pred_label)


    vote_counts = Counter(preds)
    final_prediction = vote_counts.most_common(1)[0][0]
    return final_prediction
# if __name__ == "__main__":
#     sample_text = """
#     Experienced backend software engineer with expertise in Java, microservices, cloud infrastructure, and system design.
#     """
#     prediction = ensemble_predict(sample_text)
#     print(f"Predicted Job Role: {prediction}")
