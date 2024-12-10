from flask import Flask, jsonify, abort, send_file
# TODO: Rename?
from test_grammar import generate_resume
import os
from flask_cors import CORS
import uuid

TMP_FOLDER = "tmp"

app = Flask(__name__)
CORS(app)

@app.route('/resume', methods=['POST'])
def generate():
    try:
        if not os.path.exists(TMP_FOLDER):
            os.makedirs(TMP_FOLDER)
        
        random_token = str(uuid.uuid4())
        
        token_folder = os.path.join(TMP_FOLDER, random_token)
        os.makedirs(token_folder, exist_ok=True)
        
        generate_resume(token_folder)
        return jsonify({"success": True, "token": random_token})
    except Exception as e:
        return jsonify({"success": False, "error": e})
    
@app.route('/resume/<token>', methods=['GET'])
def get_resume(token):
    # this is probably insecure... but whatever. It's local anyways
    token_folder = os.path.join(TMP_FOLDER, token)
    pdf_file = os.path.join(token_folder, "generated_resume.pdf")
    
    if not os.path.exists(pdf_file):
        return abort(404, description="Resume not found")
    
    return send_file(pdf_file, as_attachment=True, download_name=f"{token}_resume.pdf")

if __name__ == '__main__':
    app.run(debug=True)
