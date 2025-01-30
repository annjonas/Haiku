from typing import List
import uvicorn
import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Haiku(BaseModel):
    line1: str
    line2: str
    line3: str


class HaikuResponse(BaseModel):
    haiku_list: List[Haiku]


def get_random_string(length_of_string: int):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length_of_string))
    return random_string


@app.get("/haiku/", response_model=HaikuResponse)
async def haiku(number: int):
    haiku_list = []
    for _ in range(number):
        haiku_list.append(Haiku(line1=get_random_string(5), line2=get_random_string(7), line3=get_random_string(5)))
    return HaikuResponse(haiku_list=haiku_list)


class ClearQueueResponse(BaseModel):
    success: bool


class QueueSizeResponse(BaseModel):
    size: int


@app.delete("/clear/")
def clear_queue():
    return ClearQueueResponse(success=False)


@app.get("/qsize/")
def queue_size():
    return QueueSizeResponse(size=0)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
