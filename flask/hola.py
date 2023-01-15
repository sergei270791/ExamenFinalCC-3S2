from flask import Flask

app = Flask(__name__)

@app.route('/hola')
def index():
    return 'Hola Amigos CC-3S2'

app.run(host='0.0.0.0', port=8080)
