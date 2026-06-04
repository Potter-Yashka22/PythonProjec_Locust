import random
from linecache import cache

from locust import HttpUser, task, between, SequentialTaskSet


class UserFlow(SequentialTaskSet):  # список задач для пользователя которого мы имитируем
    @task
    def open_home(self): # главная страица
        self.client.get('/get')

    @task
    def check_ip(self): # проверка IP
        self.client.get('ip')

    @task
    def send_post(self): # Пользователи отправляют данные
        p={'username':'user123'}
        self.client.post('/post',json=p)

    @task
    def status_code(self): # Получаем статус-код
        spisok=[200,300,404,500]
        code=random.choice(spisok)
        # сделали скрипт чтобы все статус-коды в т.ч. 404 и 500 не считались ошибками
        with self.client.get(f'/status/{code}', catch_response=True) as response:
            if response.status_code in spisok:
                response.success()
            else:
                response.failure('error')
        # self.client.get(f'/status/{code}')
        self.interrupt() # команда означает повторять заново весь цикл


class Webuser(HttpUser): # наш пользователь
    host = 'https://httpbin.org/'
    wait_time = between(0.5,3)
    tasks = [UserFlow] # выдаем ему список задач




















