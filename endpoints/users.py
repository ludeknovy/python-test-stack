from requests import Response

from . import BaseEndpoint

DEFAULT_HEADERS = {"accept": 'application/json'}


class Users(BaseEndpoint):

    def __init__(self, client=None, x_test_id=None, **kwargs):
        super(Users, self).__init__(client, x_test_id, **kwargs)

    def create_user(self, **kwargs) -> Response:
        return self.post("/v3/user", **kwargs)

    def get_user(self, username, **kwargs) -> Response:
        return self.get(f"/v3/user/{username}", **kwargs)
