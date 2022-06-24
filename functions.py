from fastapi import FastAPI,File,UploadFile
from database_wala import *

app=FastAPI()
@app.get('/')
async def root():
    pass

#1 -> student, 2 -> student, 3 -> parents

@app.get("/2/{admno}&{var]/assignments/")
async def student_assignment(admno:str,var:str):
    x=login(persona=2,login_data=tuple(admno,var))["login"]
    if x==True:
        number=assignments.get_lastassignment_no(get_class(admno))
    else: pass

@app.post("/1/{id}&{var}/upload-assignment/{class_name}/")
async def upload_assignment(id:str,var:str,class_name:str,file: bytes = File(default=None)):
    x=login(persona=1,login_data=(tuple(id,var)))["login"]
    if x==True:
        number = int(assignments.get_lastassignment_no(self=assignments,class_name=class_name))
        path = assignments.make_assignment(self=assignments,class_name=class_name, assgno=number)["path"]
        print(path)  # idk what is the optput here thats why there is "pass" in conditions
        if path == "Error":
            pass
        else:
            f1 = open(path, "w")
            file1 = file.decode('UTF-8')
            f1.write(file1)
        return {"process":"Completed"}
    else:
        return {"process":"Failed"}

