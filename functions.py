from fastapi import FastAPI,File,UploadFile
from fastapi.responses import FileResponse
from database_wala import *

app=FastAPI()
@app.get('/')
async def root():
    pass

#1 -> teacher, 2 -> student, 3 -> parents

@app.get("/2/{admno}&{var]/assignments/")
async def student_assignment(admno:str,var:str):
    x = login(var=var, id=admno, persona=2).data()["login"]
    if x==True:
        class_name=get_class(admno)
        number=int(assignments.get_lastassignment_no(class_name))
        if number<=5:
            d=get_assignments(0,number,class_name),
        else:
            d=get_assignments(number-5,number)
        return d
    else:
        return {"Error":"incorrect id or password"}

@app.post("/2/{admno}&{var}/assignments/{assg_no}/")
async def open_assignment(admno:str,var:str,assg_no:int):
    x = login(var=var, id=admno, persona=2).data()["login"]
    if x==True:
        path=get_filepath(admno=admno)
        return {"file":FileResponse(path=path, filename="assignment{}.txt".format(assg_no))}
    else:
        return {"Error": "incorrect id or password"}



@app.post("/1/{id}&{var}/upload-assignment/{class_name}/")
async def upload_assignment(id:str,var:str,class_name:str,file: bytes = File(default=None)):
    x = login(var=var, id=id, persona=2).data()["login"]
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
