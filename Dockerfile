FROM nginx:alpine

RUN apk add --no-cache python3 py3-pip

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python3", "app.py"]
