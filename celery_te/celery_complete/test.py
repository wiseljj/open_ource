from proj.tasks import task1
from proj.tasks import task2
from proj.tasks import task3
from celery import group

# 将多个signature放入同一组中
my_group = group((task1.s(10, 10), task2.s(20, 20), task3.s(30, 30)))
ret = my_group() # 执行组任务
print(ret.get())  # 输出每个任务结果