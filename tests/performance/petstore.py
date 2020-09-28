from locust import HttpUser, task, between, events
from faker import Faker
from jtl_listener import JtlListener
fake = Faker()


class User(HttpUser):
    wait_time = between(0, 0)
    host = 'http://localhost'


    @task
    def create_new_pet(self):
        name: str = fake.name()
        payload = {
            "name": name,
            "url": name.replace(" ", "_").lower()
        }
        self.client.post("/v3/pet", json=payload)


@events.init.add_listener
def on_locust_init(environment, **_kwargs):
    JtlListener(env=environment)