from locust import HttpUser,task, between

class TestUser(HttpUser):
    wait_time = between(0.5,3)
    host = 'https://www.saucedemo.com/'

    @task
    def test1(self):
        self.client.get(self.host)
















