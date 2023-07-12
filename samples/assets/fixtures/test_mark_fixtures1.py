import pytest
"""
    Precondition
        Setup, Connection, API
    Test1
    Test3
    Assertion
    Postcondition
        clean, close
    Note: pre and post condition are common across test, we do not need to write again and again, use fixtures        
"""

@pytest.fixture
def setup():
    print("start browser (fixture)")
    yield
    print("close browser (yield)")
    
def test_1(setup):
    print("Test 1 executed")

def test_2(setup):
    print("Test 2 executed")

def test_3(setup):
    print("Test 3 executed")


