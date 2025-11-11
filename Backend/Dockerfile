#immagine iniziale versione compatta
FROM python:3.12.0-slim

WORKDIR /app


COPY requirements.txt .

RUN python -m pip install --upgrade pip \
    && python -m pip install -r requirements.txt

COPY . /app


CMD ["python", "app.py"]

