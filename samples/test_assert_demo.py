# content of test_module.py
import pytest

@pytest.fixture(scope="module", params=["mod1", "mod2"])
def modarg(request):
    param = request.param
    print("  SETUP modarg", param)
    yield param
    print("  TEARDOWN modarg", param)

@pytest.fixture(scope="function", params=[1, 2])
def otherarg(request):
    param = request.param
    print("  SETUP otherarg", param)
    yield param
    print("  TEARDOWN otherarg", param)

def test_0(otherarg):
    #print("  RUN test0 with otherarg", otherarg)
    assert "  RUN test0 with otherarg", otherarg

def test_1(modarg):
    #print("  RUN test1 with modarg", modarg)
    assert "  RUN test1 with modarg", modarg

def test_2(otherarg, modarg, tc_setup_auto):
    assert f"  RUN test2 with otherarg {otherarg} and modarg {modarg}"
