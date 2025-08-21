from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__)

# Root endpoint
@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Backend API!"})

# Hello endpoint
@app.route('/api/hello', methods=['GET'])
def hello():
    response = {"message": "Hello, ECS Backend!"}
    return jsonify(response)

# Greet endpoint
@app.route('/api/greet/<name>', methods=['GET'])
def greet(name):
    response = {"message": f"Hello, {name}! Welcome to ECS backend."}
    return jsonify(response)

# Favicon route (optional)
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
