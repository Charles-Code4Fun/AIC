# Decentralized Computing System

This system will allow tasks to be distributed across multiple worker nodes in a decentralized manner, where each worker performs its assigned task and the result is returned to the master node. We will also discuss each module in detail and provide a working demo for testing the system.

## Components of the System:
Master Node: The central control node that schedules tasks and distributes them to workers. It also collects the results after execution.
Worker Nodes: These nodes are responsible for performing the computation tasks assigned by the master node.
Broker (Redis): Redis will be used as the message broker for communication between the master and worker nodes. It handles queuing the tasks and delivering them to the workers.

```bash
pip install celery redis
```

### Linux
```bash
sudo apt install redis-server
sudo systemctl enable redis-server
sudo systemctl start redis-server
```

