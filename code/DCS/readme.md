# Decentralized Computing System

This system will allow tasks to be distributed across multiple worker nodes in a decentralized manner, where each worker performs its assigned task and the result is returned to the master node. We will also discuss each module in detail and provide a working demo for testing the system.

## Components of the System:
Master Node: The central control node that schedules tasks and distributes them to workers. It also collects the results after execution.
Worker Nodes: These nodes are responsible for performing the computation tasks assigned by the master node.
Broker (Redis): Redis will be used as the message broker for communication between the master and worker nodes. It handles queuing the tasks and delivering them to the workers.

```bash
pip install celery redis
```
## Redis
To have Redis installed and running locally or on a server.
### Linux
```bash
sudo apt install redis-server
sudo systemctl enable redis-server
sudo systemctl start redis-server
```
### Windows
for windows, please check https://github.com/microsoftarchive/redis/releases

## Define the celery Configuration
This module configures Celery and connects to Redis. It sets up the broker and backend for handling task queues and storing results.

## Redis Server
Ensure that Redis is running. Start Redis with the following command:

```bash
redis-server
```

### Start Worker Nodes
In a terminal, start the worker nodes by running the following command:

```bash
celery -A celery_config worker --loglevel=info
```
This will start the worker and listen for tasks coming from the master.

Run the Master Node
Now, execute the master node script to dispatch tasks to the workers and collect the results.
```bash
python master.py
```
The master node will send tasks to the worker nodes, and the worker will process them and send the results back.

### Demo Output
```bash
Task 1 result: 100
Task 2 result: 12
```
