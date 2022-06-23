import os
import json
import sys

import requests
from dotenv import load_dotenv

load_dotenv()
class login:
    run=0
    def t_login(self):
        id=os.getenv("id")
        if self.run==0:
            pswd=input("Enter your password: ")
        elif self.run in range(1,5):
            print("Retry login... {} chances left".format(5-self.run))
            pswd=input("Enter your password: ")
        else:
            print("Contact technical support to reset your password.")
            sys.exit(0)
        resp=requests.get('http://127.0.0.1:8000/{}/{}&{}'.format(self.value,id,pswd))
        check=json.loads(resp.text)
        if check['value']==True:
            print("login successful")
            self.run=0
        elif check['value']==False:
            print("Wrong password")
            self.run+=1
            self.t_login()
        else:
            print("contact the technical support and report an issue")

    def __init__(self, val:int):
        self.value=val
        self.t_login()

login(x) # replace x with 1-teacher, 2-students, 3-parents.
