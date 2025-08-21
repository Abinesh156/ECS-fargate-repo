from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    response = {
        "message": "Hello, ECS Backend!"
    }
    return jsonify(response)

@app.route('/api/greet/<name>', methods=['GET'])
def greet(name):
    response = {
        "message": f"Hello, {name}! Welcome to ECS backend."
    }
    return jsonify(response)

if __name__ == '__main__':
    # Run on 0.0.0.0 to allow external connections
    app.run(host='0.0.0.0', port=80)
