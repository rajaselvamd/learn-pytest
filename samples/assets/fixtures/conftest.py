import pytest

@pytest.fixture
def tc_setup():
    #global driver
    print("start browser (fixture)")
    #driver = webdriver.Chrome(ChromeDriverManager().install())
    #driver = webdriver.Chrome()
    #driver.maximize_window()
    yield
    print("close browser (yield fixture)")
    #driver.quit()

@pytest.fixture(scope="session", autouse=False)
def tc_setup_auto():
    print("start browser - from fixture autouse")
    yield
    print("close browser - after yield from fixture autouse")
