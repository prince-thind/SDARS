from fastapi import FastAPI,File,UploadFile
from fastapi.responses import FileResponse
from database_functions import *

app=FastAPI()
@app.get('/')
async def root():
    return{"functions status":"login working"}

@app.post("/login/")
async def login(username:str,password:str,person:str):
    response=check_password(username=username,password=password,person=person)
    return response


#-----------------------------------------------------------------------------------------------------------------------

@app.get("/students/circulars/")
async def student_circulars():
    pass

@app.get("/parents/circular/")
async def parent_circulars():
    pass