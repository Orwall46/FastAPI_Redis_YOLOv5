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
cd FastAPI_Redis_YOLOv5
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

## Launch app, start redis backend

Proceed to REDIS folder and run the app, then go to url
```
cd FastAPI_Redis_YOLOv5
```
```
uvicorn main:app --reload
```
```
http://127.0.0.1:8000/
```
```
python back.py
```

## Every refresh [PAGE](http://127.0.0.1:8000/result), if we have a some results, we will see a new_image with hidden number. 

