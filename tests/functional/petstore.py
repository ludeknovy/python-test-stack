from hypothesis import settings, HealthCheck
import schemathesis
import pytest

from hamcrest import assert_that, not_

from endpoints.api_tester import ApiTester
from utils.matchers.status_code_matcher import returned_status_code
from utils.request_utils import schemathesis_case_kwargs_update

schema = schemathesis.from_uri("http://localhost/v3/swagger.json")


def test_create_user(api_tester: ApiTester):
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


def test_get_existing_user(api_tester: ApiTester):
    response = api_tester.users.get_user("user1")
    assert_that(response, returned_status_code(200))


def test_get_unexisting_user(api_tester: ApiTester):
    response = api_tester.users.get_user("test")
    assert_that(response, returned_status_code(404))


@pytest.mark.property_test
@settings(deadline=None, suppress_health_check=[HealthCheck.function_scoped_fixture])
@schema.parametrize(method="GET", endpoint="/v3/user/{username}[^/]*$")
def test_get_user_no_server_errors(case, api_tester: ApiTester):
    response = api_tester.users.request(**case.as_requests_kwargs())
    assert_that(response, not_(returned_status_code(500)))