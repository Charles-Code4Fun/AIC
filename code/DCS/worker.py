# worker.py

from celery_config import app  # Import the Celery app instance

# This will start the worker and listen for tasks
if __name__ == "__main__":
    app.start()  # Starts the worker node
