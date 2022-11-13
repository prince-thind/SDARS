import mysql.connector as connector

db = connector.connect(host="127.0.0.1", user="root", password="291005", database="project")
cursor = db.cursor(buffered=True)


# ======================================================================================================================

class check_password:
    # using same cursor as defined in the file

    def __init__(self, username: str, password: str, privilege: str):
        self.username = username  # this function just defines the parameters given as self variables
        self.password = password  # these self variables are accessible by all the functions inside this class
        self.privilege = privilege
        self.cursor = cursor

    def student_login(self):
        temp_data = find_class(self.username)
        if temp_data == "?":
            raise KeyError
        command = "select * from class{} where admno={}".format(temp_data, self.username)
        self.cursor.execute(command)  # extracts the data that has been provided by execution of command
        data = (self.cursor.fetchone()[-1])
        if data == self.password:
            self.resp = True
        else:
            self.resp = False

    def teacher_login(self):
        command = "select * from faculty where id={}".format(self.username)
        self.cursor.execute(command)  # extracts the data that has been provided by execution of command
        data = self.cursor.fetchone()
        if type(data) == None:
            raise KeyError
        if data == self.password:
            self.resp = True
        else:
            self.resp = False

    def parent_login(self):
        temp_data = find_class(self.username)
        command = "select * from class{} where admno={}".format(temp_data, self.username)
        self.cursor.execute(command)  # extracts the data that has been provided by execution of command
        data = (self.cursor.fetchone()[-1])
        if data == self.password:
            self.resp = True
        else:
            self.resp = False

    def data(self):
        persons = {"student": self.student_login, "teacher": self.teacher_login, "parent": self.parent_login}
        # defining dictionary of functions that are simply callable as a reference to them is added

        try:
            persons[self.privilege]()

        except KeyError:
            self.resp = "not found"

        finally:
            return {"exists": self.resp}


# ======================================================================================================================

def find_class(username: str):
    global cursor  # using same cursor as defined in the file
    cursor.execute("show tables;")
    tables = cursor.fetchall()[0:2]
    response = "?"
    for i in tables:
        cursor.execute("select * from {} where admno='{}'".format(i[0], username))
        r_val = cursor.fetchall()  # extracts the data that has been provided by execution of command
        if len(r_val) == 1:
            response = i[0][-3:]  # change index value as per need in here
            break
        else:
            continue
    return response
