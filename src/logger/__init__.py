import logging
import os
from pathlib import Path

# Replace from_root() local function (no external dependency required)
def from_root():
    # project root = two levels up from this file
    return Path(__file__).resolve().parents[2]

from src.constant.training_pipeline import ARTIFACT_DIR, LOG_DIR, LOG_FILE, PIPELINE_NAME

logs_path = os.path.join(from_root(), PIPELINE_NAME, ARTIFACT_DIR, LOG_DIR)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)

logging = logging
