import pytest
import pdb

pdb.set_trace()
@pytest.fixture(params=("user1", "user2"))
def param_input(request):
    print(request.param)

def test_1(param_input):
    print("login test_1 ",param_input)

@pytest.mark.parametrize("a,b,sum", [(7,5,12), (6,9,16), (5,10,15)])
def test_2(a,b,sum):
    assert a+b == sum
    