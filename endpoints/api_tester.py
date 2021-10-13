from endpoints.users import Users


class ApiTester(object):
    def __init__(self, x_test_id=None, client=None):
        self.users: Users = Users(client=client, x_test_id=x_test_id)
