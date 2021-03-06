from celery import Celery

# 我们这里案例使用redis作为broker
app = Celery('demo',backend='redis://:Tencredis5.0$@@111.229.125.15:6379/7',
             broker='redis://:Tencredis5.0$@@111.229.125.15:6379/6')

# 创建任务函数
@app.task
def my_task(a,b):
    print("任务函数正在执行....")
    return a+b

#在celery_demo1目录下执行 celery -A celery_demo worker --loglevel=info    -P eventlet
#在其他地方调用mytask(a,b)时就可以异步调用了