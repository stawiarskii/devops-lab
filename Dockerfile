# Zmieniamy bazę na wersję Alpine (lżejsza i szybsza)
FROM nginx:alpine

# W Alpine używamy 'apk' zamiast 'apt-get'
# Instalujemy Pythona i PIPa
RUN apk add --no-cache python3 py3-pip

# Tworzymy środowisko wirtualne (tak jak poprzednio)
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Reszta bez zmian
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python3", "app.py"]
