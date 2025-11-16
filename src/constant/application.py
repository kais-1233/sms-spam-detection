import os

# If running inside Docker, this variable exists automatically
IS_DOCKER = os.environ.get("IS_DOCKER", "0") == "1"

if IS_DOCKER:
    APP_HOST = "0.0.0.0"   # Docker
else:
    APP_HOST = "127.0.0.1" # Local Windows

APP_PORT = 8000
