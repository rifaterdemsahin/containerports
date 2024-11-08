from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    port = request.environ.get('SERVER_PORT')
    if port == '80':
        return 'Hello from port 80!'
    elif port == '443':
        return 'Hello from port 443!'
    elif port == '8080':
        return 'Hello from port 8080!'
    elif port == '9090':
        return 'Hello from port 9090!'
    else:
        return 'Hello from an unknown port!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)