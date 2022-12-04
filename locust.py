import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task(1)
    def hello_world(self):
        self.client.get("https://flask-ci-cd.azurewebsites.net")
     @task(2)
    def on_start(self):
        self.client.post("https://flask-ci-cd.azurewebsites.net:443/predict")
