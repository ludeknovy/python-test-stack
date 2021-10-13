from hamcrest import assert_that

from utils.matchers.status_code_matcher import returned_status_code


def test_create_user(api_tester):
    response = api_tester.users.create_user(json={
        "id": 0,
        "username": "myUsername",
        "firstName": "myFirstName",
        "lastName": "myLastName",
        "email": "myEmail@test.com",
        "password": "myPassword",
        "phone": "+420606123",
        "userStatus": 0
    })
    assert_that(response, returned_status_code(200))


def test_get_existing_user(api_tester):
    response = api_tester.users.get_user("user1")
    assert_that(response, returned_status_code(200))

def test_get_unexisting_user(api_tester):
    response = api_tester.users.get_user("test")
    assert_that(response, returned_status_code(404))
