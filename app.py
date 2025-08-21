from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, ECS!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)  # Bind to all IPs and listen on port 80
