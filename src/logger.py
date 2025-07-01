import logging
import os
from datetime import datetime

# Step 1: Create a log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Step 2: Set the folder where logs will be saved
logs_path = os.path.join(os.getcwd(), "logs")  # ✅ Just "logs" folder

# Step 3: Create the folder if it doesn't exist
os.makedirs(logs_path, exist_ok=True)

# Step 4: Full path to the log file inside the logs folder
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Step 5: Configure the logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

