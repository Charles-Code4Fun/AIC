# celery_config.py

from celery import Celery

# Create a Celery instance
app = Celery('distributed_computing', broker='redis://localhost:6379/0', backend='redis://localhost:6379/1')

# Define a task in the system
@app.task
def square(x):
    """
    A simple task that computes the square of a number.
    """
    return x * x

@app.task
def fun(x, y):
    """
    A simple task that adds two numbers.
    """
    return x + y
