"""This example for testing Redis with FastAPI"""


import redis
from fastapi import FastAPI, Request, Response, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request,):
    '''Return home page with basic func'''
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/high")
async def high(request: Request, image: bytes = File(...)):
    '''Add to Redis for work'''
    with redis.Redis() as client:
        client.lpush('image', image)
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/result")
def get_results():
    '''Take a answer from redis and show on page.
    Every refresh page -> new photo, if redis has some results
    '''
    with redis.Redis() as client:
        if client.keys('answer'):
            return Response(client.brpop('answer')[1], media_type="image/png")
        return {'message': 'Oops. Dont have any results'}
