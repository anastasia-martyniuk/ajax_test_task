import logging
import subprocess
import time

import pytest
from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from utils.android_utils import android_get_desired_capabilities


@pytest.fixture(scope="session")
def logger() -> logging.Logger:
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


@pytest.fixture(scope='session')
def run_appium_server(logger):
    subprocess.Popen(
        ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure', 'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )
    logger.info("Appium REST http interface listener started on 0.0.0.0:4723")
    time.sleep(5)


@pytest.fixture(scope='session')
def driver(run_appium_server, logger) -> WebDriver:
    driver = webdriver.Remote('http://localhost:4723/wd/hub', android_get_desired_capabilities())
    logger.info("Create a new instance of the WebDriver.")
    yield driver
