from fastapi import FastAPI

app=FastAPI()
@app.get('/')
async def root():
    pass

@app.get('/{personas}/{id}&{variable}/')
async def root(personas:int,id:str, variable:str):
    if personas==1:
        from school_sql import teachers_log
        return{'value':teachers_log(id, variable)}
    elif personas==2:
        from school_sql import students_log
        return {'value': students_log(id, variable)}
    elif personas==3:
        from school_sql import parents_log
        return {'value': parents_log(id, variable)}
    else: return {'value':"ValueError"}
