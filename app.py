from flask import Flask
import redis

app = Flask(__name__)

cache = redis.Redis(host='redis', port=6379)


@app.route('/')
def hello():
    try:
        count = cache.incr('hits')
        return f"Witaj na produkcji! Ta strona zostala odwiedzona {count} razy.\n"
    except redis.exceptions.ConnectionError:
        return "Witaj! Aplikacja dziala, ale nie moze polaczyc sie z baza Redis.\n"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
