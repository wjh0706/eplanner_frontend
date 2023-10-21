from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return "Eplanner Main Page"

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('build/static', path)

if __name__ == '__main__':
    app.run(port=5000)