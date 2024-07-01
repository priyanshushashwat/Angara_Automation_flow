import os
import logging
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Angara.utils import locators

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# File Handler
file_handler = logging.FileHandler("test_log.log")
file_handler.setLevel(logging.INFO)

# Stream Handler
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# Add Handlers to Logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def close_popup_if_present(driver, wait):
    try:
        # Wait for the popup to appear and close it (Modify the selector as needed)
        popup_close_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, locators.pop_up))
        )
        popup_close_button.click()
        logger.info("Popup closed.")
    except TimeoutException:
        logger.info("No popup appeared.")


def clear_file_if_exists(file_path):
    """Function to check if a file exists and clear its contents."""
    if os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.truncate(0)
            logger.info("log file cleared")
