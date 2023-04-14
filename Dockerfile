FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install simple-websocket
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000
EXPOSE 12345

CMD ["python", "app.py"]

