from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Wersja 2.0 - CI/CD działa automatycznie!</h1>"

if __name__ == '__main__':
    # Uruchamiamy na porcie 8080 i na wszystkich interfejsach (0.0.0.0)
    app.run(host='0.0.0.0', port=8080)
