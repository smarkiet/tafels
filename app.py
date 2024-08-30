import os
from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)
app.template_folder = os.path.abspath('templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/get_question', methods=['POST'])
def get_question():
    tafel = int(request.form['tafel'])
    getal = random.randint(1, 10)
    antwoord = tafel * getal
    return jsonify({'vraag': f"{tafel} x {getal} = ?", 'antwoord': antwoord})

if __name__ == '__main__':
    app.run(debug=True)
