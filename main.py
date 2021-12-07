from locust import HttpUser, task, between

class User(HttpUser):

    time = between(1, 5)
    host = 'https://reqres.in/api'

    @task(1)
    def listUsers(self):
        self.client.get("/users")

    @task(3)
    def createSingleUser(self):
        self.client.post("/users", json={
            "name": "Alex",
            "job": "Khomenko"
        })

    @task(3)
    def updateUser(self):
        self.client.put("/users", json={
            "name": "Alex",
            "surname": "Khomenko Junior"
        })

    @task(1)
    def deleteUser(self):
        self.client.delete("/users/2")

