import time
import os
import logging
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Angara.PageObjects.commonPageObjects import close_popup_if_present, clear_file_if_exists
from Angara.utils import locators, config

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


def test_e2e_flow_to_checkout(setUp):
    wait = WebDriverWait(setUp, 50)

    # Clear the file before test execution
    clear_file_if_exists(config.log_file_path)

    # Close any pop-up if present
    close_popup_if_present(setUp, wait)

    # Click on Pendents
    pendents = setUp.find_element(By.XPATH, locators.pendents)
    pendents.click()
    logger.info("Click on Pendents")

    # Wait for search results to load
    wait.until(EC.presence_of_element_located((By.XPATH, locators.search_result)))

    # Click on the first product
    first_product = setUp.find_elements(By.XPATH, locators.search_result)[0]
    first_product.click()
    logger.info("Click on first result")

    # Wait for product page to load
    wait.until(EC.presence_of_element_located((By.XPATH, locators.add_to_cart)))

    # Click the "Add to Cart" button
    setUp.find_element(By.XPATH, locators.add_to_cart).click()
    logger.info("Click on add to cart.")

    # Check out
    time.sleep(20)
    setUp.find_element(By.XPATH, locators.checkout).click()

    # Enter contact info
    setUp.find_element(By.XPATH, locators.email).send_keys(config.email)
    logger.info("Enter email: %s", config.email)
    setUp.find_element(By.XPATH, locators.first_name).send_keys(config.first_name)
    logger.info("Enter First Name: %s", config.first_name)
    setUp.find_element(By.XPATH, locators.last_name).send_keys(config.last_name)
    logger.info("Enter Last Name: %s", config.last_name)
    setUp.find_element(By.XPATH, locators.address).send_keys(config.address)
    logger.info("Enter Address: %s", config.address)
    setUp.find_element(By.XPATH, locators.city).send_keys(config.city)
    logger.info("Enter City: %s", config.city)
    setUp.find_element(By.XPATH, locators.pin).send_keys(config.pin)
    logger.info("Enter Pin: %s", config.pin)
    setUp.find_element(By.XPATH, locators.phone).send_keys(config.phone)
    logger.info("Enter Phone: %s", config.phone)
    setUp.find_element(By.XPATH, locators.save_shipping_information_checkbox).click()

    # Verify on the checkout page
    assert "Checkout" in setUp.title
    logger.info("Test Passed: Reached checkout page.")
