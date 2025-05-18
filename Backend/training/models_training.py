import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import csr_matrix, hstack
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import joblib


df = pd.read_csv('../datasets/balanced_resumes.csv')

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

def extract_weighted_features(texts, weighted_kws_dict):
    features = {}
    for category, kws_weights in weighted_kws_dict.items():
        features[category] = texts.apply(lambda x: weighted_keyword_score(x, kws_weights))
    return pd.DataFrame(features)

X = df['cleaned_resume']
y = df['job_category']

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)
joblib.dump(label_encoder, '../models/label_encoder.pkl')

X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
)

X_train_kw = extract_weighted_features(X_train, weighted_keywords)
X_test_kw = extract_weighted_features(X_test, weighted_keywords)

tfidf = TfidfVectorizer(ngram_range=(1,3), stop_words='english')
X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)
joblib.dump(tfidf, '../models/tfidf_vectorizer.pkl')

X_train_kw_sparse = csr_matrix(X_train_kw.values)
X_test_kw_sparse = csr_matrix(X_test_kw.values)

X_train_combined = hstack([X_train_tfidf, X_train_kw_sparse])
X_test_combined = hstack([X_test_tfidf, X_test_kw_sparse])

models = {
    'logistic_regression': LogisticRegression(max_iter=1000, class_weight='balanced'),
    'random_forest': RandomForestClassifier(n_estimators=100, class_weight='balanced'),
    'xgboost': XGBClassifier(use_label_encoder=False, eval_metric='mlogloss'),
    'lightgbm': LGBMClassifier(n_estimators=100)
}

for name, model in models.items():
    print(f"\nTraining {name}...")
    model.fit(X_train_combined, y_train)
    y_pred = model.predict(X_test_combined)

    print(f"Classification Report for {name}:")
    print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))

    # Plot confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(7,5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=label_encoder.classes_,
                yticklabels=label_encoder.classes_)
    plt.title(f'{name} Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.show()

    joblib.dump(model, f"{name}.pkl")
    print(f"Saved model: {name}.pkl")

print("\nAll models trained, evaluated, and saved successfully.")
