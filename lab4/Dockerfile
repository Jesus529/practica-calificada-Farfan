FROM python:3.11-slim

LABEL maintainer="kevin.vargas.c@tecsup.edu.pe"
LABEL description="Mi primera aplicación Docker"

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
