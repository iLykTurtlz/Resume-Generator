from flask import Flask, jsonify, abort, send_file, send_from_directory
# TODO: Rename?
from test_grammar import generate_resume
import os
from flask_cors import CORS
import uuid

RESUME_FOLDER = "resumes"

app = Flask(__name__, static_folder="build/static")
CORS(app)

@app.route('/resumes', methods=['POST'])
def generate():
    try:
        if not os.path.exists(RESUME_FOLDER):
            os.makedirs(RESUME_FOLDER)
        
        random_token = str(uuid.uuid4())
        
        token_folder = os.path.join(RESUME_FOLDER, random_token)
        os.makedirs(token_folder, exist_ok=True)
        
        generate_resume(token_folder)
        return jsonify({"success": True, "token": random_token})
    except Exception as e:
        return jsonify({"success": False, "error": e})
    
@app.route('/resumes/<token>', methods=['GET'])
def get_resume(token):
    # this is probably insecure... but whatever. It's local anyways
    token_folder = os.path.join(RESUME_FOLDER, token)
    pdf_file = os.path.join(token_folder, "generated_resume.pdf")
    
    if not os.path.exists(pdf_file):
        return abort(404, description="Resume not found")
    
    return send_file(pdf_file, as_attachment=True, download_name=f"{token}_resume.pdf")

@app.route("/resumes", methods=["GET"])
def get_resume_tokens():
    try:
        tokens = [
            folder for folder in os.listdir(RESUME_FOLDER)
            if os.path.isdir(os.path.join(RESUME_FOLDER, folder))
        ]
        return jsonify({"success": True, "tokens": tokens}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


# React stuff
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react_app(path):
    return send_from_directory(os.path.join(app.root_path, 'build'), 'index.html')

if __name__ == '__main__':
    app.run(debug=True, port=6969)
