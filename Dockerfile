FROM python:3-slim

WORKDIR /app

CMD ["sh", "-c", "pip install --no-cache-dir -r requirements.txt && gunicorn --bind 0.0.0.0:5001 app:app"]
