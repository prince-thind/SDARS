import mysql.connector as conn
db=conn.connect(host="127.0.0.1",user="root",password="291005", database="school")
cursor=db.cursor(buffered=True)

def teachers_log(id,var):
    cursor.execute("select * from faculty where id='{}'".format(id))
    data=(cursor.fetchone()[2])
    if data==var:
        return True
    else: return False
def students_log(id,var):
    cursor.execute("select * from students where admno='{}'".format(id))
    data=(cursor.fetchone()[-1])
    print(data)
    if data==var:
        return True
    else: return False
def parents_log(id,var):
    cursor.execute("select * from students where admno='{}'".format(id))
    data=(cursor.fetchone()[-1])
    if data==var:
        return True
    else: return False


def get_class(admno:str):
    global cursor
    cursor.execute("show tables;")
    temp=cursor.fetchall()
    for i in temp:
        cursor.execute("select * from {} where admno='{}';".format(i[0], admno))
        data=cursor.fetchall()
        if len(data)==1:
            resp= str(i[0])
            break
        else:
            resp= "not in database"
            continue
    return resp
