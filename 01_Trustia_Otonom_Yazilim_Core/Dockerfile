# TRUSTIA Otonomi Platformu — Docker Container Yapılandırması
FROM python:3.12-slim

WORKDIR /app

# Bağımlılıklar (Yalnızca NumPy)
RUN pip install --no-cache-dir numpy pytest

# Proje dosyalarını kopyala
COPY . /app

# Çevre değişkenleri
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# Varsayılan Çalıştırma Komutu (Test Süiti)
CMD ["python", "-m", "pytest"]
