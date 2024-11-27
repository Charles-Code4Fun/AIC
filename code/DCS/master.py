# master.py

from celery_config import square, add  # Import the tasks from the configuration
import time

def main():
    # Dispatching tasks to the worker
    # result1 = square.apply_async((10,))  # Sending task to square the number 10
    # result2 = add.apply_async((5, 7))    # Sending task to add 5 and 7

    # Assign the task to specific queues
    result1 = square.apply_async((10,), queue='square_queue')
    result2 = add.apply_async((5, 7), queue='add_queue')
    
    # Wait for the results
    print(f"Task 1 result: {result1.get(timeout=10)}")
    print(f"Task 2 result: {result2.get(timeout=10)}")

if __name__ == "__main__":
    main()
