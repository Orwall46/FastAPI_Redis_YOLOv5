# Redis with YOLOv5 based on FastAPI app

## Description

The project acquaints with the [Redis](https://redis.io), a simple Python library for jobs and processing them in the background with workers.

## Technologies

- Python3;
- FastAPI web-framework;
- Redis;
- PIP virtual environment;
- YOLOv5
- Pillow

## Installation

### Prerequisites
Install [Redis](https://redis.io) and [Python3](https://www.python.org) on your computer. 
Use pip for virtual environment.
If u don't wanna install Redis, u can run with Docker [Docker_Redis](https://hub.docker.com/_/redis)
 
### Then go to a command line
Clone repository and navigate to folder on command line:
```
git clone ...
```
```
cd REDISQ
```

Install dependencies, run virtual environment
```
python -m venv .venv (for example)
```
```
cd .venv/scripts
```
```
activate
```
```
pip install -r requirements.txt
```

Start Redis-server and check if Redis is working properly (response is PONG)
```
redis-server
```
```
redis-cli ping
```

## Launch, start app

Proceed to rq-demo/rq_demo folder and run the app, then go to url
```
cd REDISQ
```
```
uvicorn main:app --reload
```
```
http://127.0.0.1:8000/
```
