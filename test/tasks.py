# from celery import Celery, group, chord
#
# app = Celery('tasks', broker='redis://localhost:6379/0')
#
# @app.task
# def print_message(message):
#     print(message)
#
#
# group_of_tasks = group(
#     print_message.s("M1"),
#     print_message.s("M2"),
#     print_message.s("M3"),
# )
# print(group_of_tasks)
# final_task = chord(group_of_tasks)
# result = final_task.delay()


# from celery import Celery, group, chord
#
# app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')
#
# @app.task
# def print_message(message):
#     print(message)
#     return message
#
#
# group_of_tasks = group(
#     print_message.s("M1"),
#     print_message.s("M2"),
#     print_message.s("M3"),
# )
# print(group_of_tasks)
# final_task = chord(group_of_tasks)
# result = final_task.delay()
#
# output = result.get()
# print(output)


# from celery import Celery, group, chord
#
# app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')
#
# @app.task
# def print_message(message):
#     print(message)
#     return message
#
#
# group_of_tasks = group(
#     print_message.s("M1"),
#     print_message.s("M2"),
#     print_message.s("M3"),
# )
# print(group_of_tasks)
# final_task = chord(group_of_tasks)
# result = final_task.delay()
#
# output = result.get()
# print(output)




# from celery import Celery, group, chord
#
# app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')
#
#
# @app.task
# def print_message(message):
#     print(message)
#     return message
#
#
# group_of_tasks = group(
#     print_message.s("M1"),
#     print_message.s("M2"),
#     print_message.s("M3"),
# )
# print(group_of_tasks)
#
# for task in group_of_tasks.tasks:
#     print(task.args)
# final_task = chord(group_of_tasks)
# result = final_task.delay()
#
# output = result.get()
# print(output)


from celery import Celery, group

# app = Celery('tasks', broker='pyamqp://guest@localhost//')
app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

@app.task
def add(x, y):
    return x + y

@app.task
def multiply(x, y):
    return x * y

@app.task
def subtract(x, y):
    return x - y

results = group(add.s(2, 2), multiply.s(3, 4), subtract.s(10, 5))().get()
total = sum(results)

print(results)
print(total)
