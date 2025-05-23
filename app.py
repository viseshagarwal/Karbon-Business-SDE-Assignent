from flask import Flask, render_template, request, redirect, jsonify
from model import probe_model_5l_profit
import json
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)

    try:
        # Read the uploaded file directly into memory
        content = file.read()
        data = json.loads(content)

        # Call model function to get evaluated financial flags
        flags = probe_model_5l_profit(data["data"])
        # print(flags)

        # Instead of saving the result to a file, you can pass it directly to the template
        return render_template('results.html', flags=flags)
    except Exception as e:
        # Handle any exceptions that may occur during the process
        return render_template('error.html', error_message=str(e))


if __name__ == '__main__':
    app.run(debug=True)
