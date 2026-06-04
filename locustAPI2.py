
import random

from locust import  HttpUser, task, between, SequentialTaskSet


class BeginnerFlow(SequentialTaskSet):
    @task
    def open_home(self):  # главная страица
        self.client.get('/get')

    @task
    def check_ip(self):  # проверка IP
        self.client.get('ip')
        self.interrupt()


class AdvancedFlow(SequentialTaskSet):
    @task
    def open_home(self):  # главная страица
        self.client.get('/get')

    @task
    def send_post(self):  # Пользователи отправляют данные
        p = {'username': 'user123'}
        self.client.post('/post', json=p)

    @task
    def status_code(self):  # Получаем статус-код
        spisok = [200, 300, 404, 500]
        code = random.choice(spisok)
        with self.client.get(f'/status/{code}', catch_response=True) as response:
            if response.status_code in spisok:
                response.success()
            else:
                response.failure('error')
        # self.client.get(f'/status/{code}')
        self.interrupt()

class BeginnerUser(HttpUser):
    weight = 3
    host = 'https://httpbin.org/'
    wait_time = between(2, 3)
    tasks = [BeginnerFlow]

class AdvancedUser(HttpUser):
    weight = 1
    host = 'https://httpbin.org/'
    wait_time = between(0.5, 1)
    tasks = [AdvancedFlow]


