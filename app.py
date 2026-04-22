from flask import Flask
import redis

app = Flask(__name__)

# Nawiązujemy połączenie z bazą Redis
# Zauważ, że host to po prostu słowo 'redis', a nie adres IP!
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    try:
        # Próbujemy zwiększyć licznik o nazwie 'hits' w bazie
        count = cache.incr('hits')
        return f"Witaj na produkcji! Ta strona zostala odwiedzona {count} razy.\n"
    except redis.exceptions.ConnectionError:
        # Ten blok wykona się, jeśli baza Redis będzie wyłączona
        return "Witaj! Aplikacja dziala, ale nie moze polaczyc sie z baza Redis.\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)