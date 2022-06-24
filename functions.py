from fastapi import FastAPI,File,UploadFile
from database_wala import *

app=FastAPI()
@app.get('/')
async def root():
    pass

#1 -> student, 2 -> student, 3 -> parents

@app.get("/2/{admno}/assignments/")
async def student_assignment(admno:str):
    number=assignments.get_lastassignment_no(get_class(admno))

@app.post("/1/{id}/upload-assignment/{class_name}/")
async def upload_assignment(id:str,class_name:str,file: bytes = File(default=None)):
    number=int(assignments.get_lastassignment_no(class_name))
    path=assignments.make_assignment(class_name,number)["path"]
    print(path) # idk what is the optput here thats why there is "pass" in conditions
    if path=="Error":
        pass
    else:
        pass
        f1 = open(path, "w")
        file1 = file.decode('UTF-8')
        f1.write(file1)
        pass


    return {"file_len": len(file)}

