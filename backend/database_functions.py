import mysql.connector as connector

db = connector.connect(host="127.0.0.1", user="root", password="password", database="school")  # change "password" here
cursor = db.cursor(buffered=True)

#=======================================================================================================================

class login():
    global cursor

    def __init__(self,username:str,password:str,person:str):
        self.username=username
        self.password=password
        self.person=person

    def student_login(self):
        temp_data = find_class(self.username)
        if temp_data == "?":
            raise KeyError
        command = "select * from class{} where admno='{}'".format(temp_data,self.username)
        self.cursor.execute(command)
        data = (self.cursor.fetchone()[-1])
        if data == self.password:
            self.resp = True
        else:
            self.resp = False


    def teacher_login(self):                          # edit here in patch-2
        command="select * from faculty where id='{}'".format(self.username)
        self.cursor.execute(command)
        data = (self.cursor.fetchone()[2])    # what if there is no data found?
        if data == self.password:
            self.resp = True
        else:
            self.resp = False

    def parent_login(self):
        temp_data=find_class(self.username)
        if temp_data == "?":
            raise KeyError
        command = "select * from class{} where admno='{}'".format(temp_data, self.username)
        self.cursor.execute(command)
        data = (self.cursor.fetchone()[-1])
        if data == self.password:
            self.resp = True
        else:
            self.resp = False


    def data(self):
        persons={"student": self.student_login, "teacher":self.teacher_login, "parent":self.parent_login}

        try:
            persons[self.person]()

        except KeyError:
            self.resp="not found"
            pass

        finally:
            return {"exists":self.resp}

#=======================================================================================================================

def find_class(username:str):
    global cursor
    cursor.execute("show tables;")
    tables = cursor.fetchall().remove(("faculty",))
    response = "?"
    for i in tables:
        cursor.execute("select * from {} where admno='{}'".format(i[0],username))
        r_val=cursor.fetchall()
        if len(r_val)==1:
            response = i[0][-4:]                        # specific for our use
            break
        else:continue
    return response

