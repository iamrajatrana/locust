from locust import User, constant, task

class Test1(User):

    weight = 2
    wait_time = constant(1)

    @task
    def launch1(self):
        print("Launching the URL 1")

    @task
    def search1(self):
        print("Searching 1")


class Test2(User):
    
    weight = 2
    wait_time = constant(1)

    @task
    def launch2(self):
        print("Launching the URL 2")

    @task
    def search2(self):
        print("Searching 2")