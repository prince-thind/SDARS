import pickle

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import datetime

import database_functions
import file_functions
from database_functions import *

app = FastAPI()


@app.get('/')
async def root():
    return {"functions status": "working twice"}


@app.get("/login/{username}&{password}&{privilege}")
async def login(username: str, password: str, privilege: str):
    response = check_password(username=username, password=password, privilege=privilege).data()
    response["privilege"] = privilege
    return response


# -----------------------------------------------------------------------------------------------------------------------


@app.get("/students/circulars/{username}")
async def student_circulars(username: str):
    class_n_sec=find_class(username)
    if class_n_sec=="?":
        return {"data": "username not found"}
    else:
        object = file_functions.circulars(student_class=class_n_sec)
        return object.get_data()

@app.post("/teachers/circulars/{username}&{s_class}")
async def teacher_circulars(username: str, s_class: str, file: bytes = File(default=None)):
    try:
        obj = file_functions.circulars(student_class=s_class)
        path = obj.path+"\\circular_no{}.dat".format(obj.last_circular_no())
        f = open(path, "wb")
        pickle.dump(file.decode(utf-8),f)
        status = True
    except:
        status = False
    finally:
        return {"status": status}

@app.get("/parents/circulars/{username}")
async def parent_circulars(username: str):
    class_n_sec=find_class(username)
    if class_n_sec=="?":
        return {"data": "username not found"}
    else:
        object = file_functions.circulars(student_class=class_n_sec)
        return object.get_data()


# -----------------------------------------------------------------------------------------------------------------------


@app.get("/students/assignments/{username}")
async def student_assignments(username: str):
    class_n_sec = database_functions.find_class(username)
    if class_n_sec=="?":
        return {"data":"username not valid"}
    else:
        obj = file_functions.assignments(class_n_sec=class_n_sec)
        return {"data":obj.get_data()}


@app.post("/teachers/assignments/{username}&{class_n_sec}")
async def teacher_assignments(username: str, class_n_sec: str, file: bytes = File(default=None)):
    try:
        obj = file_functions.assignments(class_n_sec=class_n_sec)
        path = obj.path+"\\assignment{}.txt".format(obj.last_assgn_no()+1)
        f = open(path, "w")
        f.write(file.decode("UTF-8"))
        status = True
    except:
        status = False
    finally:
        return {"status": status}


# ======================================================================================================================


@app.post("/teachers/progress")
async def teacher_progress(username:str,subject_name:str,max_marks:int,marks_obtained:int,description:str):
    try:
        f1_obj=open(f"\\students\\{username}.dat",'ab')

        d={"date":(str(datetime.date.today().month),str(datetime.date.today().year)),"subject_name":subject_name,
           "max_marks":max_marks,"marks_obtained":marks_obtained,"description":description}

        pickle.dump(d.copy(),f1_obj)
        d.clear()
        statu=True
    except:
        statu=False
    finally:
        return {status:statu}

@app.get("/students/progress/{username}")
async def student_progress(username:str):
    f1_obj = open(f"\\students\\{username}.dat", 'rb')
    try:
        data_multiple=[]
        while True:
            data_singular=pickle.load(f1_obj).copy()
            if data_singular["date"]==(str(datetime.date.today().month),str(datetime.date.today().year)):
                del data_singular["date"]
                data_multiple.append(data_singular.copy())
            else: pass

    except EOFError:
        reponse={data:data_multiple}
    finally:
        return reponse

@app.get("/parents/progress/{username}")
async def parents_progress(username:str):
    f1_obj = open(f"\\students\\{username}.dat", 'rb')
    try:
        data_multiple = []
        while True:
            data_singular = pickle.load(f1_obj).copy()
            if data_singular["date"] == (str(datetime.date.today().month), str(datetime.date.today().year)):
                del data_singular["date"]
                data_multiple.append(data_singular.copy())
            else:
                pass

    except EOFError:
        reponse = {data: data_multiple}
    finally:
        return reponse


# ======================================================================================================================


@app.post("/teachers/attendence")
async def teachers_attendence(username:str,attendence:int,remarks:str):
    try:
        f1_obj = open(f"\\students\\{username}.txt", 'w')
        f1_obj.write(f"attendence={attendence}\nremarks={remarks}")
        statu=True
    except:
        statu=False
    finally:
        return {status:statu}

@app.get("/students/attendence/{username}")
async def students_attendence(username:str):
    f1_obj = open(f"\\students\\{username}.txt", 'r')
    temp=f1_obj.readlines()
    attendence_d=temp[0].replace("attendence=","")
    remarks_d=temp[1].replace("remarks=","")
    return {data:[{name:username,remarks: remarks_d , attendence: int(attendence_d)}]}

@app.get("/parents/attendence/{username}")
async def parents_assignments(username:str):
    f1_obj = open(f"\\students\\{username}.txt", 'r')
    temp = f1_obj.readlines()
    attendence_d = temp[0].replace("attendence=", "")
    remarks_d = temp[1].replace("remarks=", "")
    return {data: [{name: username, remarks: remarks_d, attendence: int(attendence_d)}]}
