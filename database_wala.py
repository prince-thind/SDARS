import mysql.connector as conn
db = conn.connect(host="127.0.0.1", user="root", password="291005", database="school")
cursor = db.cursor(buffered=True)

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
            self.cursor.execute("insert into {} values({},'{}')".format(class_name, assgno, path))
            self.db.commit()
            return {"path":path}
        except:
            return {"path":"Error"}



#---------------------------------------------------------------------------------------------------------------------

class login:
    db = conn.connect(host="127.0.0.1", user="root", password="291005", database="school")
    cursor = db.cursor(buffered=True)
    def __init__(self, var:str,id:str,persona:int):
        self.id = id
        self.var = var
        self.persona = persona


    def data(self):
        try:

            if self.persona == 1:
                self.teachers_log()
            elif self.persona == 2:
                self.students_log()
            elif self.persona == 3:
                self.parents_log()
            else:
                raise ValueError
        except ValueError:
            self.resp="False"
        except:
            self.resp="failed"
        finally:
            return {"login":self.resp}

    def teachers_log(self):
        self.cursor.execute("select * from faculty where id='{}'".format(self.id))

        data = (self.cursor.fetchone()[2])
        if data == self.var:
            print("here")
            self.resp=True
        else:
            self.resp=False

    def students_log(self):
        command = "select * from {} where admno='{}'".format(get_class(self.id), self.id)
        self.cursor.execute(command)
        data = (self.cursor.fetchone()[-1])
        if data == self.var:
            self.resp = True
        else:
            self.resp = False

    def parents_log(self):
        command="select * from {} where admno='{}'".format(get_class(self.id), self.id)
        self.cursor.execute(command)
        data = (self.cursor.fetchone()[-1])
        if data == self.var:
            self.resp = True
        else:
            self.resp = False

 #---------------------------------------------------------------------------------------------------------------------
def get_class(admno: str):
        global cursor
        cursor.execute("show tables;")
        temp = cursor.fetchall()
        resp = "not in database"
        for i in temp:
            cursor.execute("select * from {} where admno='{}';".format(i[0], admno))
            data = cursor.fetchall()
            if len(data) == 1:
                resp = str(i[0])
                break
            else:
                continue
        return resp

def get_assignments(start: int, end: int, class_name: str):
        d = dict()
        for x in range(start, end + 1):
            path = "assignments_{}/assignment{}.txt".format(class_name, x)
            with open(path, 'r') as file:
                data = file.read().split("\n")
                topic = data[1].split('=')[1]
                subject = data[0].split('=')[1]
                d[subject] = topic
        return d
def get_filepath(number,admno):
        class_name=get_class(admno)
        path="assignments_{}/assignment{}.txt".format(class_name, number)
        return path
