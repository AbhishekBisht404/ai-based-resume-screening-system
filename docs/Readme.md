# 🧠 AI-Based Resume Screening System

A smart resume screening system that leverages Natural Language Processing (NLP), Machine Learning (ML), and custom Named Entity Recognition (NER) models to analyze resumes and provide feedback, score candidates, and predict suitable job roles.

## 🚀 Tech Stack

- ⚙️ **Backend**: Python, FastAPI  
- 📚 **NLP & ML**:
  - Custom-trained spaCy NER model for skill extraction  
  - Multiple ML models (Logistic Regression, Random Forest, XGBoost, LightGBM) for job role prediction  
  - TF-IDF, keyword features, and voting ensemble   
- 🌐 **Frontend**: React + Vite + TypeScript + Tailwind CSS  
- 🔍 PDF resume parsing and scoring system  
- 📦 Git LFS for handling large model files  

## ✨ Features

- ✅ Resume upload and parsing  
- ✅ Job role prediction using ensemble ML models  
- ✅ Custom skill extraction with NER  
- ✅ Resume scoring based on relevance and skill matching  
- ✅ Suggestions and detailed feedback report generation  
- ✅ Responsive frontend with modern UI (React + Vite)  

## 📁 Project Structure (Backend)

```
├── Backend/
│   ├── .idea/                            # IDE configuration files
│   ├── .ipynb_checkpoints/              # Jupyter notebook checkpoints
│   ├── .venv/                           # Python virtual environment
│   ├── custom_parser.py                 # Custom parser for resumes
│   ├── datasets/                        # Dataset files
│   ├── data_processing/                 # Data cleaning and processing scripts
│   ├── EDA/                            # Exploratory Data Analysis notebooks/scripts
│   ├── job_role_predictor.py            # ML model for job prediction
│   ├── main.py                         # FastAPI backend entry point
│   ├── models/                         # ML and NER models
│   ├── report_generator.py             # Generates feedback reports
│   ├── requirements.txt                # Python dependencies
│   ├── scoring_resume.py               # Resume scoring logic
│   ├── suggestions_generator.py       # Generates suggestions based on scoring
│   ├── tmp_trainer/                    # Temporary training files
│   ├── training/                      # Model training scripts/files
│   └── __pycache__/                    # Python cache files
├── Frontend/
│   ├── .DS_Store                         
│   ├── .idea/                           
│   ├── ai-resume-analyzer-frontend/     # Main frontend app (React + Vite)
│   │   ├── node_modules/                # Installed dependencies
│   │   ├── package.json                 # Project metadata and scripts
│   │   ├── package-lock.json            # Exact versions of installed dependencies
│   │   ├── tsconfig.json                # TypeScript configuration
│   │   └── src/                         # Application source code
│   │       ├── App.tsx                  # Root component of the React application
│   │       └── components/              # Reusable UI components
│   │           └── ui/                  # Shared UI elements (buttons, inputs, etc.)
├── .gitignore  
└── README.md  
```

## 📦 Setup Instructions
## 🚀 How to Install and Initialize

### 1. Clone the repository

```bash
git clone https://github.com/AbhishekBisht404/ai-based-resume-screening-system.git
cd ai-based-resume-screening-system

### 🔧 Backend (FastAPI)
```
```bash
cd Backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload
```

### 🌐 Frontend (React + Vite)

```bash
cd Frontend
npm install
npm run dev
```

## 🧪 Demo Features (In Progress)

- [ ] Authentication & user dashboard  
- [ ] Admin panel to manage job categories  
- [ ] Improved NER with domain-specific tagging  
- [ ] Graphical resume feedback report  

## 📜 License

MIT License  

---

### 🙌 Contributing

Pull requests are welcome! If you're interested in contributing, feel free to open issues or submit a PR.

---

### ⭐ Star this repo if you like it!
