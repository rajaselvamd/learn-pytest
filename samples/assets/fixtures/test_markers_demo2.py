import pytest
import sys

@pytest.mark.skip
def test_login():
    print("login done")

# custom marker, declared in pytest.ini
@pytest.mark.smoke
def test_init():
    print("init of application")

@pytest.mark.skipif(sys.version_info<(3,12), reason="python version not supported")
def test_addProduct():
    print("add product")

#An xfail means that you expect a test to fail for some reason
@pytest.mark.xfail
def test_logout():
    assert False
    print("Logout done")    

@pytest.mark.xfail
def test_close():
    assert True
    print("Close the application")    

