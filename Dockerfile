FROM python:3.8-slim-bookworm

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    wget \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip setuptools wheel

# Tell Python app that it's running inside Docker
ENV IS_DOCKER=1

WORKDIR /app
COPY . /app

# Install Python dependencies with retries & timeout
RUN pip install --default-timeout=300 --retries=10 -r requirements.txt

CMD ["python3", "app.py"]
