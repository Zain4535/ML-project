import logging
import os
from datetime import datetime

# Create a folder named "log"
LOG_FOLDER = "log"
os.makedirs(LOG_FOLDER, exist_ok=True)

# Create a unique log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Full file path
LOG_FILE_PATH = os.path.join(LOG_FOLDER, LOG_FILE)

# Configure logger
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

