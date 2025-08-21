from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, ECS!"

if __name__ == '__main__':
    # Run on 0.0.0.0 to allow external connections
    app.run(host='0.0.0.0', port=80)
