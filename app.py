# app.py
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
import json
from model import probe_model_5l_profit

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        with open(file_path, 'r') as f:
            data = json.load(f)
        result = probe_model_5l_profit(data['data'])
        os.remove(file_path)  # Remove the uploaded file after processing
        return jsonify(result)


@app.route('/results')
def results():
    return render_template('results.html')


if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
