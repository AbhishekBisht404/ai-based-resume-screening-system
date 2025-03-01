AI-Based Resume Screening System

📌 Overview

This project is an AI-powered Resume Screening System that helps filter and rank resumes based on job descriptions using Natural Language Processing (NLP) and Machine Learning. The system consists of:

AI Model: Processes resumes and extracts relevant information.

Backend: Built with Node.js and Express.js for API handling.

Frontend: A React-based user interface for interaction.

🛠️ Tech Stack

🔹 AI Model

Python

FastAPI

SpaCy

Scikit-Learn

OpenAI GPT (optional for advanced screening)

🔹 Backend

Node.js

Express.js

MySQL/MongoDB (for storing resumes and results)

🔹 Frontend

React.js / Next.js

Tailwind CSS

📂 Project Structure

AI-Based-Resume-Screening-System/
│── ai_model/               # AI model scripts (Python)
│── backend/                # Backend (Node.js + Express)
│── frontend/               # Frontend (React/Next.js)
│── .gitignore              # Ignored files
│── README.md               # Documentation
│── requirements.txt        # Python dependencies
│── package.json            # Node.js dependencies

🚀 Getting Started

🔹 1. Clone the Repository

git clone https://github.com/your-username/ai-resume-screening.git
cd ai-resume-screening

🔹 2. Setting up the AI Model

cd ai_model
python -m venv .venv
source .venv/bin/activate  # (For macOS/Linux)
.venv\Scripts\activate     # (For Windows)
pip install -r requirements.txt

Run the AI model:

uvicorn main:app --reload

🔹 3. Setting up the Backend

cd backend
npm install
npm start

🔹 4. Setting up the Frontend

cd frontend
npm install
npm run dev

📜 Features

✔️ Resume parsing & keyword extraction
✔️ Job description matching
✔️ Candidate ranking based on AI
✔️ Web dashboard for recruiters

📌 TODO



🛡️ Security & Best Practices

Use .env for secrets & API keys.

Enable GitHub branch protection.

Keep dependencies updated.

📩 Contributing

Want to improve this project? Feel free to fork & contribute!

git checkout -b feature-branch
git commit -m "Your Changes"
git push origin feature-branch

📄 License

This project is licensed under the MIT License. 
