from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse

import database_functions
import file_functions
from database_functions import *

app = FastAPI()


@app.get('/')
async def root():
    return {"functions status": "login working"}


@app.get("/login/{username}&{password}&{privilege}")
async def login(username: str, password: str, privilege: str):
    response = check_password(username=username, password=password, privilege=privilege).data()
    response["privilege"] = privilege
    return response


# done to the end part just testing left

# -----------------------------------------------------------------------------------------------------------------------

@app.get("/students/circulars/{username}")
async def student_circulars(username: str):
    class_n_sec=find_class(username)
    if class_n_sec=="?":
        return {"data": "username not found"}
    else:
        object = file_functions.circulars(student_class=class_n_sec)
        return object.get_data()


# done just need to setup circular folder

@app.post("/teachers/circulars/{username}&{s_class}")
async def teacher_circulars(username: str, s_class: str, file: bytes = File(default=None)):
    try:
        obj = file_functions.circulars(student_class=s_class)
        path = obj.path+"\\circular_no{}".format(obj.last_circular_no())
        f = open(path, "w")
        f.write(file.decode("UTF-8"))
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
async def teacher_progress():
    pass
