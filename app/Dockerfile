FROM python:alpine3.7

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_RUN_PORT 5000

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .
CMD ["flask", "run"]
