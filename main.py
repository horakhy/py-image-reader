from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Hello, World!'})

@app.route('/processImage', methods=['POST'])
def processImage():
    t_id = request.form['id']
    t_name = request.form['name']
    return jsonify({'message': f'{t_id}, {t_name}!'})

app.run()