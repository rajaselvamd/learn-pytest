import pytest

# Arrange
@pytest.fixture
def first_entry():
    return "a"

@pytest.fixture
def second_entry():
    return 2

# Arrange
@pytest.fixture
def order(first_entry, second_entry):
    return [first_entry, second_entry]

# Arrange
@pytest.fixture
def expected_list():
    return ["a", 2, 3.0]

def test_string1(order, expected_list):
    # Act
    order.append(3.0)

    # Assert
    assert order == expected_list

def test_string2(order):
    # Act
    order.append("b")

    # Assert
    assert order == ["a", 2, "b"]

def test_string3(order, expected_list):
    # Act
    order.append("c")

    # Assert
    assert order == expected_list

