import mysql.connector as conn


class assignments:
    db = conn.connect(host="127.0.0.1", user="root", password="291005", database="assignments")
    cursor=db.cursor()
    def get_lastassignment_no(self,class_name:str):
        self.cursor.execute("select * from {};".format(class_name))
        num = self.cursor.fetchall()
        if len(num) == 0:
            return 0
        else:
            return num[0][0]

    def make_assignment(self,class_name: str, assgno:int):
        try:
            path = 'C:\\Users\\Sumit\\PycharmProjects\\csproject\\assignments_{}\\assignment{}'.format(class_name,
                                                                                                       assgno)
            self.cursor.execute("insert into {} values({},{})".format(class_name, assgno, path))
            return {"path":path}
        except:
            return {"path":"Error"}



class login:
    db = conn.connect(host="127.0.0.1", user="root", password="291005", database="school")
    cursor = db.cursor(buffered=True)

    def __init__(self, id:str, var:str, persona:int):
        self.id = id
        self.var = var
        try:
            if persona == 1:
                resp = self.teachers_log()
            elif persona == 2:
                resp = self.students_log()
            elif persona == 3:
                resp = self.parents_log()
            else:
                raise ValueError
        except ValueError:
            resp="False"
        except:
            resp="Contact Administrator"
        finally:
            self.final_response={"login":resp}


    def teachers_log(self):
        self.cursor.execute("select * from faculty where id='{}'".format(self.id))
        data = (self.cursor.fetchone()[2])
        if data == self.var:
            return True
        else:
            raise ValueError

    def students_log(self):
        command = "select * from {} where admno='{}'".format(get_class(self.id), self.id)
        self.cursor.execute(command)
        data = (self.cursor.fetchone()[-1])
        if data == self.var:
            return True
        else:
            raise ValueError

    def parents_log(self):
        command="select * from {} where admno='{}'".format(get_class(self.id), self.id)
        self.cursor.execute(command)
        data = (self.cursor.fetchone()[-1])
        if data == self.var:
            return True
        else:
            raise ValueError

def get_class(admno:str):
    global cursor
    cursor.execute("show tables;")
    temp=cursor.fetchall()
    resp = "not in database"
    for i in temp:
        cursor.execute("select * from {} where admno='{}';".format(i[0], admno))
        data=cursor.fetchall()
        if len(data)==1:
            resp= str(i[0])
            break
        else:
            continue
    return resp
