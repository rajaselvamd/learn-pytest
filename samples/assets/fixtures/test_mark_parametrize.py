import pytest

@pytest.mark.parametrize("username, password",
                         [
                             ("selenium", "seladmin"),
                             ("pytest", "pytadmin"),
                             ("db", "dbadmin"),
                         ]
                         )
def test_login(username, password):
    print(username, password)
