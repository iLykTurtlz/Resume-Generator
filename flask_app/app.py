from flask import Flask, render_template, jsonify


app = Flask(__name__)


@app.route('/')
def resume():
    return render_template('resume.html')  # Your HTML page template with a button

@app.route('/get_resume_data', methods=['GET'])
def get_resume_data():
    resume_data = {
        "name": "Hadi Asemi",
        "email": "hadi@example.com",
        "phone": "+1 123-456-7890",
        "location": "San Francisco, CA",
        "summary": "A dedicated and skilled cybersecurity pentester with a strong foundation in computer science and specialized training in API security...",
        "experience": [
            {
                "title": "Senior Associate",
                "company": "Motive-Power",
                "dates": "2022 - Present",
                "description": "Focused on cybersecurity and software engineering, providing secure and efficient solutions to clients."
            },
            {
                "title": "Software Engineer",
                "company": "TechCorp",
                "dates": "2020 - 2022",
                "description": "Worked on building scalable backend systems and improving security protocols."
            }
        ],
        "education": [
            {
                "degree": "B.S. in Computer Science",
                "school": "Cal Poly SLO",
                "year": "2019"
            }
        ],
        "skills": [
            "Python", "Flask", "Cybersecurity", "Cloud Administration", "DevOps"
        ]
    }
    return jsonify(resume_data)  # Return resume data as JSON




if __name__ == '__main__':
    app.run(debug=True)

