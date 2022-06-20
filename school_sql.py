import mysql.connector as conn
db=conn.connect(host="127.0.0.1",user="root",password="291005", database="school")
cursor=db.cursor()

def teachers_log(id,var):
    cursor.execute("select * from faculty where id='{}'".format(id))
    data=(cursor.fetchone()[2])
    if data==var:
        return True
    else: return False
def students_log(id,var):
    cursor.execute("select * from students where admno='{}'".format(id))
    data=(cursor.fetchone()[-1])
    if data==var:
        return True
    else: return False
def parents_log(id,var):
    cursor.execute("select * from students where admno='{}'".format(id))
    data=(cursor.fetchone()[-1])
    if data==var:
        return True
    else: return False
