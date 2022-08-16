from celery import Celery, chain

job_queue_app = Celery(
    'tasks', broker="redis://127.0.0.1:6379/0", backend="redis://127.0.0.1:6379/1")
chain(
            job_queue_app.signature("f1", args=["ehsan"]).set(queue="f1"),
            job_queue_app.signature("f2", args=[]).set(queue="f2"),
        ).apply_async()

chain(
            job_queue_app.signature("sum", args=[10, 20]).set(queue="sum"),
            job_queue_app.signature("mul", args=[2, 5]).set(queue="mul"),
            job_queue_app.signature("report", args=[]).set(queue="report"),
        ).apply_async()


app = Celery(
    "tasks", broker="redis://127.0.0.1:6379/0", backend="redis://127.0.0.1:6379/1"
)


app.conf.task_routes = {
    "app.tasks.f1": {"queue": "f1"},
    "app.tasks.f2": {"queue": "f2"}
}


@app.task(name="f1")
def f1(name):
    print(f'Hi, {name} from f1')
    return f'Hi, {name}'


@app.task(name="f2")
def f2(hi):
    print(f'Hi string is: {hi}')


@app.task(name="sum")
def sum(a, b):
    print(f'Sum of them is {a + b}')
    return a + b


@app.task(name="mul")
def mul(sum_output, a, b):
    print(f'Multiply of them is {a * b}')
    return sum_output, a + b


@app.task(name="report")
def report(mul_output):
    s, m = mul_output
    s = f'''
        Sum of two numbers: {s}
        Multiply of two numbers: {m}
    '''
    print(s)
