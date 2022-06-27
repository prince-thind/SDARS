from fastapi import FastAPI,File,UploadFile
from fastapi.responses import FileResponse
from database_wala import *

app=FastAPI()
@app.get('/')
async def root():
    pass

#1 -> teacher, 2 -> student, 3 -> parents
# yesssss!!! uncommented code. breakyour mind understanding this mess

@app.get("/2/{admno}&{var]/assignments/")
async def student_assignment(admno:str,var:str):
    x = login(var=var, id=admno, persona=2).data()["login"]
    if x==True:
        class_name=get_class(admno)
        number=int(assignments.get_lastassignment_no(self=assignments,class_name=class_name))
        if number<=5:
            d=get_assignments(0,number,class_name),
        else:
            d=get_assignments(number-5,number,class_name)
        return d
    else:
        return {"Error":"incorrect id or password"}

@app.post("/{persona}/{admno}&{var}/assignments/{assg_no}/")
async def open_assignment(persona:int,admno:str,var:str,assg_no:int):
    x = login(var=var, id=admno, persona=persona).data()["login"]
    if x==True:
        path=get_filepath(admno=admno,assignment_no=assg_no)
        return {"file":FileResponse(path=path, filename="assignment{}.txt".format(assg_no))}
    else:
        return {"Error": "incorrect id or password"}

@app.post("/1/{id}&{var}/upload-assignment/{class_name}/")
async def upload_assignment(id:str,var:str,class_name:str,file: bytes = File(default=None)):
    x = login(var=var, id=id, persona=2).data()["login"]
    if x==True:
        number = int(assignments.get_lastassignment_no(self=assignments,class_name=class_name))
        path = assignments.make_assignment(self=assignments,class_name=class_name, assgno=number)["path"]
        if path == "Error":
            return {"process": "uploading failed"}
        else:
            f1 = open(path, "w")
            file1 = file.decode('UTF-8')
            f1.write(file1)
            resp_path=path+"_response"
            resp=open(resp_path)
            resp.write("response of assignment number {}\n".format(number))
            resp.close()
            f1.close()

        return {"process":"Completed"}
    else:
        return {"process":"login Failed"}
#---------------------------------------------------------------------------------------------------------------------

@app.post("/1/{id}&{var}/upload-circular/{class_name}")
async def upload_circular(id:str,var:str,class_name:str,file:bytes = File(default=None)):
    x=login(var=var, id=id, persona=2).data()["login"]
    if x==True:
        try:
            path = last_circular_number(class_name)
            f = open(path, "w")
            f.write(file.decode("UTF-8"))
            f.close()
            value="Completed"
        except: value="uploading failed"
    else: value="login failed"
    return {"process":value}

@app.post("/{persona}/{admno}&{var}/get_circulars/{circ_no}/")
async def open_assignment(persona:int,admno:str,var:str,circ_no:int):
    x = login(var=var, id=admno, persona=persona).data()["login"]
    if x==True:
        path="C:\\Users\\Sumit\\PycharmProjects\\csproject\\circular_{}\\circular_no{}.txt".format(get_class(admno),circ_no)
        return {"file":FileResponse(path=path, filename="circular_no{}.txt".format(circ_no))}
    else:
        return {"process":"login failed"}

@app.get("/{persona}/{admno}&{var]/circulars/")
async def circulars(persona:int,admno: str, var: str):
    x = login(var=var, id=admno, persona=persona).data()["login"]
    if x == True:
        class_name = get_class(admno)
        number = int(last_circular_number(class_name))
        if number <= 5:
            d = get_circulars(0, number, class_name)
        else:
            d = get_circulars(number - 5, number, class_name)
    else:
        d = "login failed"
    return {"process": d}
#---------------------------------------------------------------------------------------------------------------------------

@app.get("/2/{admno}&{var}/test_results/{test_name}")
async def test_result(admno:str,var:str,test_name:str):
    x = login(var=var, id=admno, persona=2).data()["login"]
    if x==True:
        path="C:\\Users\\Sumit\\PycharmProjects\\csproject\\results_{}\\{}.txt".format(get_class(admno),test_name)
        return {"file": FileResponse(path=path, filename="{}.txt".format(test_name))}
    else:
        return {"process": "login failed"}

@app.get("/2/{admno}&{var}/recent_tests/")
async def recent_tests(admno:str,var:str):
    x = login(var=var, id=admno, persona=2).data()["login"]
    if x == True:
        class_name=get_class(admno)
        raw_data=test_names(class_name)
        names=raw_data[0]
        test_nos=raw_data[1]
        if test_nos <=6:
            return {"process":names}
        else:
            return {"process":names[-6:]}
