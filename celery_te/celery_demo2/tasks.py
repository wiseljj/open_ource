from main import app

@app.task()
def fun(a,b):
    return a+b
