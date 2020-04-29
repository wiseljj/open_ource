from celery import Celery

app=Celery('demo')
app.config_from_object('proj.celeryconfig')
app.autodiscover_tasks(['proj'])


# 在celery_complete文件夹下执行celery -A proj worker -l info  -P eventlet
#在其他地方调用mytask1(a,b)时就可以异步调用了