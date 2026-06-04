

from sel import *
from locust import User, task, between
import time

class WebUser(User):
    wait_time = between(0.5,3)
    host = 'https://www.saucedemo.com/'

    def on_start(self):
        options = Options()
        # options.add_argument('--headless')
        self.driver = webdriver.Firefox(options=options)
        self.driver.implicitly_wait(5)
        pass

    def on_stop(self):
        self.driver.quit()
        pass

    @task
    def test_reg(self):
        start_time = time.time()
        try:
            self.driver.get('https://www.saucedemo.com/')
        except TimeoutException:
            print('сайт не грузится до конца')
        toSend(self.driver, By.ID, 'user-name', 'standard_user')
        toSend(self.driver, By.ID, 'password', 'secret_sauce')
        toClick(self.driver, By.ID,'login-button')

        try:
            # Explicit verification step
            if "/inventory.html" in self.driver.current_url:
                total_time = int((time.time() - start_time) * 1000)
                # Report success to the Locust interface
                self.environment.events.request.fire(
                    request_type="Selenium",
                    name="Inv Load",
                    response_time=total_time,
                    response_length=0,
                    exception=None,
                    context={}
                )
            else:
                raise Exception("Page title did not match expectation.")
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            # Report failure to the Locust interface
            self.environment.events.request.fire(
                request_type="Selenium",
                name="Homepage Load",
                response_time=total_time,
                response_length=0,
                exception=e,
                context={}
            )


















