from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
   wait_time = between(1, 5)


   @task
   def login(self):
       self.client.post("/api/auth/login", json={
           "email": "yasinalbayrak@sabanciuniv.edu",
           "password": "yasin123"
       }, headers={
           "Accept": "application/json, text/plain, */*",
           "Accept-Language": "en-US,en;q=0.9",
           "Connection": "keep-alive",
           "Content-Type": "application/json",
           "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
       }, verify=False)




from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
   wait_time = between(1, 5)


   @task
   def register(self):
       self.client.post("/api/auth/register", json={
           "email": "newuser@gmail.com",
           "password": "newuser123",
           "username": "newuser"
       }, headers={
           "Accept": "application/json, text/plain, */*",
           "Accept-Language": "en-US,en;q=0.9",
           "Connection": "keep-alive",
           "Content-Type": "application/json",
           "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
       }, verify=False)


if __name__ == "__main__":
   import os
   import locust
   os.system("locust -f locustfile.py --host=http://104.198.25.207:5001")


