FROM python:3.11-slim

LABEL maintainer="tu-email@ejemplo.com"
LABEL description="Descargador de videos"

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

RUN mkdir -p downloads

EXPOSE 5000

CMD ["python", "app.py"]