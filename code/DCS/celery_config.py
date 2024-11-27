# celery_config.py

from celery import Celery
from celery.exceptions import Retry

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
def add(x, y):
    """
    A simple task that adds two numbers.
    """
    return x + y


@app.task(bind=True, max_retries=3)
def square_AutoTry(self, x):
    try:
        if x < 0:
            raise ValueError("Negative numbers are not allowed")
        return x * x
    except Exception as e:
        raise self.retry(exc=e)
