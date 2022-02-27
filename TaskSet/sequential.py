from locust import HttpUser, SequentialTaskSet, constant, task

class MyTaskSet(SequentialTaskSet):

    @task
    def test1(self):
        self.client.get("/200")
        print("Get Status of 200")


    @task
    def test2(self):
        self.client.get("/500")
        print("Get Status of 500")



class Main(HttpUser):
    host = "https://http.cat"
    tasks = [MyTaskSet]
    wait_time = constant(1)
