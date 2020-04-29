from celery import Celery

app=Celery('demo2')
app.config_from_object('celeryconfig')
# app.autodiscover_tasks(['proj'])


# 在celery_demo2文件夹下执行celery -A tasks worker -l info  -P eventlet
#在其他地方调用task(a,b)时就可以异步调用了