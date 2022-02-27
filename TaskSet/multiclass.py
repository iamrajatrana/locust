from locust import HttpUser, TaskSet, constant, task

class MyHttpCat(TaskSet):
    
    @task
    def get_status(self):
        self.client.get("/200")
        print("Get Status of 200")
        self.interrupt(reschedule=False)

    @task
    def get_random_status(self):
        self.client.get("/201")
        print("Get Status of 201")
        self.interrupt(reschedule=False)


class MyAnotherHttpCat(TaskSet):
        
    @task
    def get_500_status(self):
        self.client.get("/500")
        print("Get Status of 500")
        self.interrupt(reschedule=False)



class Test(HttpUser):

    host = "https://http.cat"
    tasks = [MyHttpCat, MyAnotherHttpCat]
    wait_time = constant(1)

    
# if no self interrupt, will not switch class once one gets executed