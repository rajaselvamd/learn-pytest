import pytest
import sys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

"""
    fixture with selenium web browser call
"""

driver = None
#sys.stdin.reconfigure(encoding='utf-8')
#sys.stdout.reconfigure(encoding='utf-8')

@pytest.fixture
def setup():
    global driver
    print("start browser (fixture)")
    #driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome()
    #driver.maximize_window()
    yield
    print("close browser (yield)")
    driver.quit()
    
def test_1(setup):
    driver.get("http://www.google.com")
    print("Test 1 executed")

def test_2(setup):
    driver.get("https://www.opera.com/")
    print("Test 2 executed")

def test_3(setup):
    driver.get("https://www.mozilla.org")
    print("Test 3 executed")


