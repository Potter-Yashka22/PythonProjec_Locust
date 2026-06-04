
from locust import HttpUser,task,between


class Sandboxer(HttpUser):
    wait_time = between(1,3)
    host = 'https://happydog.by/'

    @task
    def test_page(self):
        self.client.get(self.host)









