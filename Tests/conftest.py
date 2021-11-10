import pytest
from selenium import webdriver
from pathlib import Path
import os

@pytest.fixture(scope="class")
def init_driver(request):
     downloads_path = os.path.join(Path.home(), "Downloads", "chromedriver_win32")
     os.environ['PATH'] = downloads_path
     driver = webdriver.Chrome()
     request.cls.driver = driver
     yield
     driver.close()
     