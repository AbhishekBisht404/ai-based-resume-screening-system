from typing import List, Dict

SKILL_SUGGESTIONS = {
    'html': "Mention specific projects using HTML5 or semantic markup.",
    'css': "Highlight responsive designs or animations done with CSS.",
    'javascript': "Showcase dynamic websites or use of ES6+ features.",
    'react': "Include experience building SPAs or using React hooks.",
    'node.js': "Mention backend services or APIs created using Node.js.",
    'git': "Add version control experience, especially team collaboration with Git.",
    'python': "Highlight scripting, automation, or data analysis projects.",
    'pandas': "Include data cleaning or manipulation tasks done using Pandas.",
    'numpy': "Mention any scientific or numerical computation work.",
    'scikit-learn': "Describe ML models you've built with scikit-learn.",
    'sql': "Include queries or database operations you've written.",
    'aws': "Mention deployments or cloud services used on AWS.",
    'docker': "Describe containerizing apps and working with Dockerfiles.",
    'kubernetes': "Include orchestration tasks or production deployments.",
    'ci/cd': "Show experience setting up pipelines (e.g., GitHub Actions, Jenkins).",
    'unit testing': "Mention tools used like pytest, JUnit, or your test coverage.",
    'java': "Highlight backend services or Android development using Java.",
    'machine learning': "Include models built, algorithms used, or competitions.",
    'deep learning': "Mention use of TensorFlow/Keras and any CNN/RNN models.",
    'penetration testing': "Add tools used (e.g., Metasploit, Burp Suite) or types of tests performed.",
    'threat detection': "Describe incidents detected or alerts investigated.",
    'microservices': "Talk about services designed, communication protocols (e.g., REST, gRPC).",
    'frontend': "Mention UI frameworks, performance optimization, or UX design.",
    'backend': "Highlight APIs built, databases used, or scalability handled.",
    'data science': "Include EDA, modeling, and insights drawn from data."
}

def generate_suggestions(missing_skills: List[str]) -> Dict[str, str]:
    suggestions = {}
    for skill in missing_skills:
        normalized_skill = skill.lower().strip()
        suggestion = SKILL_SUGGESTIONS.get(
            normalized_skill,
            f"Add more detail or examples related to '{skill}' to strengthen your resume."
        )
        suggestions[skill] = suggestion
    return suggestions


# if __name__ == "__main__":
#     missing = ['React', 'Kubernetes', 'CI/CD', 'Problem Solving']
#     feedback = generate_suggestions(missing)
#     for skill, tip in feedback.items():
#         print(f"{skill}: {tip}")
