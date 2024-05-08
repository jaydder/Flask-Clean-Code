import os
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return '<h1>Hellow</h1>'



port = int(os.environ.get('PORT', 5000))
if __name__ == '__main__':
    app.run(port=port, debug=True, host="0.0.0.0")