import pytest

@pytest.fixture(autouse=True)
def tc_setup():
    print()
    print("start test (fixture) setup ")
    yield
    print("close test (yield fixture) cleanup")

@pytest.fixture(scope="session", autouse=True)
def tc_setup_auto():
    print("start test initial setup - from global conftest fixture autouse")
    yield
    print("close test, cleanup - after yield from global conftest fixture autouse")
