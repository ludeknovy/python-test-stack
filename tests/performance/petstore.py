from locust import HttpUser, task, between, events
from faker import Faker

from endpoints.api_tester import ApiTester
from jtl_listener import JtlListener
fake = Faker()


class User(HttpUser):
    wait_time = between(0, 0)
    host = "http://localhost:80"

    def on_start(self):
        self.api_tester = ApiTester(client=self.client)


    @task
    def create_new_pet(self):
        self.api_tester.users.get_user("test1")


@events.init.add_listener
def on_locust_init(environment, **_kwargs):
    JtlListener(env=environment)