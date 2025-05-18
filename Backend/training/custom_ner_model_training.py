import spacy
from spacy.training import Example
from spacy.util import minibatch, compounding
import random

def create_training_data(texts, skill_lists):
    training_data = []
    for text, skills in zip(texts, skill_lists):
        entities = []
        for skill in skills:
            start = text.find(skill)
            if start != -1:
                end = start + len(skill)
                entities.append((start, end, "SKILL"))
            else:
                print(f"Warning: '{skill}' not found in text: {text}")
        training_data.append((text, {"entities": entities}))
    return training_data

texts = [
    "Skilled in Python, Java, and React.",
    "Experienced with TensorFlow and PyTorch.",
    "Worked with AWS, Docker, and Kubernetes.",
    "Proficient in HTML, CSS, and JavaScript.",
    "Expert in C++, JavaScript, and Node.js.",
    "Worked on cloud platforms such as Azure, AWS, and GCP.",
    "Familiar with Docker and Kubernetes for containerization.",
    "Experience with SQL, MongoDB, and PostgreSQL databases.",
    "Worked with Angular, Vue.js, and React in front-end development.",
    "Knowledge of machine learning frameworks like TensorFlow and scikit-learn.",
    "Developed using Java, Spring Boot, and Hibernate for back-end applications.",
    "Experienced in working with React Native for mobile app development.",
    "Familiar with DevOps tools such as Jenkins, Docker, and Git.",
    "Worked with NoSQL databases like MongoDB, Cassandra.",
    "Skilled in Agile methodologies, Scrum, and Kanban.",
    "Experienced with Apache Kafka and RabbitMQ for messaging.",
    "Worked on data processing with Apache Spark, Hadoop, and Kafka.",
    "Proficient in Python scripting for automation and data analysis.",
    "Experience using Elasticsearch and Logstash for log management.",
    "Skilled in using Jupyter notebooks for data analysis and visualization.",
    "Knowledge of front-end technologies like HTML5, CSS3, and JavaScript.",
    "Experience with Python libraries such as Pandas, NumPy, and Matplotlib.",
    "Worked on machine learning projects using Keras, TensorFlow, and PyTorch.",
    "Familiar with RESTful APIs, JSON, and XML for data exchange.",
    "Experienced in version control with Git and GitHub.",
    "Worked on cloud infrastructure using Terraform and AWS CloudFormation.",
    "Skilled in microservices architecture using Spring Boot and Docker.",
    "Expert in SQL and PostgreSQL database management.",
    "Worked on continuous integration with Jenkins, CircleCI, and GitLab.",
    "Familiar with Agile tools like Jira and Trello.",
    "Experienced with data visualization tools like Tableau and Power BI.",
    "Proficient in using MongoDB and Redis for data storage.",
    "Worked with front-end libraries like Bootstrap and Material-UI.",
    "Skilled in using Apache Spark for big data processing.",
    "Familiar with version control systems like Git and SVN.",
    "Experience working with machine learning frameworks like XGBoost and LightGBM.",
    "Proficient in Java for building enterprise applications.",
    "Worked on data pipelines with Apache Airflow and Luigi.",
    "Skilled in front-end frameworks like Angular and React.",
    "Worked on mobile app development using Kotlin and Flutter.",
    "Experience in cloud computing with Azure and AWS.",
    "Proficient in C# and .NET framework for software development.",
    "Familiar with NoSQL databases such as Cassandra and Firebase.",
    "Worked with container orchestration using Kubernetes and Docker.",
    "Skilled in JavaScript libraries like jQuery and D3.js.",
    "Experienced in serverless architectures using AWS Lambda and Azure Functions.",
    "Proficient in Java for Android app development.",
    "Worked on data science projects using R and SAS.",
    "Experienced in working with Apache Kafka and RabbitMQ for messaging.",
    "Skilled in continuous deployment using Jenkins and CircleCI.",
    "Proficient in machine learning algorithms such as SVM, Random Forest, and Neural Networks.",
    "Experience with data processing tools such as Pandas and NumPy.",
    "Skilled in using Elasticsearch, Logstash, and Kibana for monitoring.",
    "Worked with big data tools like Hadoop and Apache Hive.",
    "Experienced in building web applications using Flask and Django.",
    "Worked on front-end development using HTML5, CSS3, and Vue.js.",
    "Familiar with machine learning platforms like Google Cloud AI and IBM Watson.",
    "Experienced in big data processing with Spark, Hadoop, and Flink.",
    "Skilled in using databases like Oracle and MongoDB.",
    "Proficient in using cloud tools like Google Cloud Platform and AWS.",
    "Worked with data visualization tools like Power BI and QlikView.",
    "Skilled in Android app development using Kotlin and Java.",
    "Experienced with Agile frameworks like Scrum and Kanban.",
    "Proficient in Python and Django for building scalable web applications.",
    "Skilled with React.js, Node.js, and MongoDB for full-stack development.",
    "Extensive experience using SQL and PostgreSQL for database management.",
    "Familiar with machine learning algorithms such as SVM, KNN, and Random Forest.",
    "Experienced in cloud technologies including AWS, Google Cloud Platform, and Azure.",
    "Worked with DevOps tools like Jenkins, Docker, and Kubernetes for continuous integration.",
    "Proficient in data visualization using Tableau, Power BI, and QlikView.",
    "Skilled in front-end technologies like HTML5, CSS3, and JavaScript.",
    "Expert in deep learning frameworks such as TensorFlow, PyTorch, and Keras.",
    "Experienced with Agile methodologies, including Scrum, Kanban, and Lean.",
    "Skilled in using Elasticsearch, Logstash, and Kibana for search and analytics.",
    "Worked on big data projects using Apache Spark, Hadoop, and Kafka.",
    "Familiar with Docker and Kubernetes for containerization and orchestration.",
    "Proficient in R and Python for data analysis and statistical modeling.",
    "Worked on microservices architecture using Spring Boot, Docker, and AWS Lambda.",
    "Skilled in using Git for version control and GitHub for code collaboration.",
    "Proficient in using IDEs like Visual Studio Code, PyCharm, and IntelliJ IDEA.",
    "Experienced in mobile app development using Kotlin and Flutter for Android and iOS.",
    "Worked with NoSQL databases like MongoDB and Cassandra for high performance storage.",
    "Familiar with cloud-native technologies like Kubernetes, Helm, and Istio.",
    "Skilled in using Apache Kafka for real-time data streaming and messaging.",
    "Experience with RESTful APIs, JSON, and XML for data exchange and integration.",
    "Proficient in server-side programming with Node.js, Express, and MongoDB.",
    "Experienced in using data processing tools like Apache Flink and Apache Storm.",
    "Skilled in Java for building enterprise applications using Spring Framework.",
    "Expert in building interactive dashboards using Power BI, Tableau, and Google Data Studio.",
    "Experience with SQL databases like MySQL, PostgreSQL, and Microsoft SQL Server.",
    "Familiar with automation tools like Ansible, Chef, and Puppet for infrastructure management.",
    "Proficient in using Apache Maven and Gradle for Java build automation.",
    "Worked on front-end technologies like Angular, Vue.js, and SASS.",
    "Skilled in data wrangling and cleaning using Python libraries like Pandas and NumPy.",
    "Experienced in business intelligence using tools like Microsoft Power BI, Tableau, and Qlik.",
    "Skilled in using Apache Hadoop for large-scale data processing and analysis.",
    "Worked with GitHub Actions and Travis CI for continuous integration and deployment.",
    "Familiar with NoSQL database technologies like CouchDB and DynamoDB.",
    "Skilled in using cloud services like AWS EC2, S3, and Lambda for scalable application deployment.",
    "Proficient in machine learning models like Decision Trees, Random Forest, and Gradient Boosting.",
    "Experienced in full-stack development with MERN (MongoDB, Express, React, Node.js).",
    "Skilled in project management using Jira, Trello, and Asana.",
    "Worked on implementing security measures using tools like Wireshark, Metasploit, and Nessus.",
    "Experienced in mobile app development using Swift for iOS and Kotlin for Android."
]

skills = [
    ["Python", "Java", "React"],
    ["TensorFlow", "PyTorch"],
    ["AWS", "Docker", "Kubernetes"],
    ["HTML", "CSS", "JavaScript"],
    ["C++", "JavaScript", "Node.js"],
    ["Azure", "AWS", "GCP"],
    ["Docker", "Kubernetes"],
    ["SQL", "MongoDB", "PostgreSQL"],
    ["Angular", "Vue.js", "React"],
    ["TensorFlow", "scikit-learn"],
    ["Java", "Spring Boot", "Hibernate"],
    ["React Native"],
    ["Jenkins", "Docker", "Git"],
    ["MongoDB", "Cassandra"],
    ["Agile", "Scrum", "Kanban"],
    ["Apache Kafka", "RabbitMQ"],
    ["Apache Spark", "Hadoop", "Kafka"],
    ["Python"],
    ["Elasticsearch", "Logstash"],
    ["Jupyter notebooks"],
    ["HTML5", "CSS3", "JavaScript"],
    ["Pandas", "NumPy", "Matplotlib"],
    ["Keras", "TensorFlow", "PyTorch"],
    ["RESTful APIs", "JSON", "XML"],
    ["Git", "GitHub"],
    ["Terraform", "AWS CloudFormation"],
    ["Spring Boot", "Docker"],
    ["SQL", "PostgreSQL"],
    ["Jenkins", "CircleCI", "GitLab"],
    ["Jira", "Trello"],
    ["Tableau", "Power BI"],
    ["MongoDB", "Redis"],
    ["Bootstrap", "Material-UI"],
    ["Apache Spark"],
    ["Git", "SVN"],
    ["XGBoost", "LightGBM"],
    ["Java"],
    ["Apache Airflow", "Luigi"],
    ["Angular", "React"],
    ["Kotlin", "Flutter"],
    ["Azure", "AWS"],
    ["C#", ".NET"],
    ["Cassandra", "Firebase"],
    ["Kubernetes", "Docker"],
    ["jQuery", "D3.js"],
    ["AWS Lambda", "Azure Functions"],
    ["Java"],
    ["R", "SAS"],
    ["Apache Kafka", "RabbitMQ"],
    ["Jenkins", "CircleCI"],
    ["SVM", "Random Forest", "Neural Networks"],
    ["Pandas", "NumPy"],
    ["Elasticsearch", "Logstash", "Kibana"],
    ["Hadoop", "Apache Hive"],
    ["Flask", "Django"],
    ["HTML5", "CSS3", "Vue.js"],
    ["Google Cloud AI", "IBM Watson"],
    ["Spark", "Hadoop", "Flink"],
    ["Oracle", "MongoDB"],
    ["Google Cloud Platform", "AWS"],
    ["Power BI", "QlikView"],
    ["Kotlin", "Java"],
    ["Scrum", "Kanban"],
    ["Python", "Django"],
    ["React.js", "Node.js", "MongoDB"],
    ["SQL", "PostgreSQL"],
    ["SVM", "KNN", "Random Forest"],
    ["AWS", "Google Cloud Platform", "Azure"],
    ["Jenkins", "Docker", "Kubernetes"],
    ["Tableau", "Power BI", "QlikView"],
    ["HTML5", "CSS3", "JavaScript"],
    ["TensorFlow", "PyTorch", "Keras"],
    ["Scrum", "Kanban", "Lean"],
    ["Elasticsearch", "Logstash", "Kibana"],
    ["Apache Spark", "Hadoop", "Kafka"],
    ["Docker", "Kubernetes"],
    ["R", "Python"],
    ["Spring Boot", "Docker", "AWS Lambda"],
    ["Git", "GitHub"],
    ["Visual Studio Code", "PyCharm", "IntelliJ IDEA"],
    ["Kotlin", "Flutter"],
    ["MongoDB", "Cassandra"],
    ["Kubernetes", "Helm", "Istio"],
    ["Apache Kafka"],
    ["RESTful APIs", "JSON", "XML"],
    ["Node.js", "Express", "MongoDB"],
    ["Apache Flink", "Apache Storm"],
    ["Java", "Spring Framework"],
    ["Power BI", "Tableau", "Google Data Studio"],
    ["MySQL", "PostgreSQL", "Microsoft SQL Server"],
    ["Ansible", "Chef", "Puppet"],
    ["Apache Maven", "Gradle"],
    ["Angular", "Vue.js", "SASS"],
    ["Pandas", "NumPy"],
    ["Microsoft Power BI", "Tableau", "Qlik"],
    ["Apache Hadoop"],
    ["GitHub Actions", "Travis CI"],
    ["CouchDB", "DynamoDB"],
    ["AWS EC2", "S3", "Lambda"],
    ["Decision Trees", "Random Forest", "Gradient Boosting"],
    ["MongoDB", "Express", "React", "Node.js"],
    ["Jira", "Trello", "Asana"],
    ["Wireshark", "Metasploit", "Nessus"],
    ["Swift", "Kotlin"],
]


TRAIN_DATA = create_training_data(texts, skills)

nlp = spacy.load('en_core_web_lg')

ner = nlp.get_pipe("ner")

ner.add_label("SKILL")

other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
with nlp.disable_pipes(*other_pipes):

    optimizer = nlp.resume_training()
    print("Starting training...")

    for iteration in range(30):
        random.shuffle(TRAIN_DATA)
        losses = {}

        batches = minibatch(TRAIN_DATA, size=compounding(4.0, 32.0, 1.5))
        for batch in batches:
            examples = []
            for text, annotations in batch:
                doc = nlp.make_doc(text)
                examples.append(Example.from_dict(doc, annotations))

            nlp.update(examples, drop=0.2, losses=losses, sgd=optimizer)

        print(f"Iteration {iteration + 1}, Losses: {losses}")
nlp.to_disk('models/custom_ner_model')
print("Training complete!")

# # Test the trained model
# test_texts = [
#     "Proficient in Python, Django, and Kubernetes.",
#     "Experienced with Java, Docker, and AWS cloud services.",
#     "Knowledge of CSS, HTML, and React.js."
#     "Experienced software engineer with 5+ years in full-stack web development. Skilled in JavaScript, React, Node.js, and Python. Proven ability to build scalable applications and lead small development teams."
# ]
#
# for text in test_texts:
#     doc = nlp(text)
#     print(f"\nText: {text}")
#     print("Entities:", [(ent.text, ent.label_) for ent in doc.ents])
