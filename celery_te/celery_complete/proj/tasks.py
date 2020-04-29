from proj.celery import app

@app.task()
def task1(a,b):
    print('执行任务1')
    return a+b

@app.task()
def task2(a,b):
    print('执行任务2')
    return a + b

@app.task()
def task3(a,b):
    print('执行任务3')
    return a + b