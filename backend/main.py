import string
import redis
import json
from typing import List
import uvicorn
import random
from fastapi import FastAPI
from pydantic import BaseModel
import requests
import asyncio
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins. Replace with ["http://localhost:3000"] for security
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

# Redis connection setup
redis_client = redis.StrictRedis(host='redis', port=6379, db=0, decode_responses=True)

words_by_request_count = 20
MAX_QUEUE_SIZE = 100  # Maximum number of haikus allowed in the queue


class Haiku(BaseModel):
    line1: str
    line2: str
    line3: str


class HaikuResponse(BaseModel):
    haiku_list: List[Haiku]

def get_random_words(count: int):
    url = "https://random-word-api.vercel.app/api?words=" + str(count) + ""
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        return []


def count_syllables(word):
    word = word.lower()
    vowels = "aeiouy"
    count = 0
    prev_char_was_vowel = False
    for char in word:
        if char in vowels:
            if not prev_char_was_vowel:
                count += 1
            prev_char_was_vowel = True
        else:
            prev_char_was_vowel = False
    if word.endswith("e") and count > 1:
        count -= 1
    return max(1, count)


def compose_line(syllables: int):
    current_syllables = 0
    result = ""
    while current_syllables < syllables:
        searched_length = syllables - current_syllables
        words = get_random_words(words_by_request_count)
        filtered_words = list(filter(lambda w: count_syllables(w) <= searched_length, words))
        if(len(filtered_words) > 0):
            found_word = filtered_words[random.randint(0, len(filtered_words) - 1)]
            found_word_syllables_count = count_syllables(found_word)
            if current_syllables == 0:
                result += found_word
                current_syllables += found_word_syllables_count
            else:
                result += " " + found_word
                current_syllables += found_word_syllables_count
    return result


def compose_haiku():
    haiku = []
    haiku.append(compose_line(5))
    haiku.append(compose_line(7))
    haiku.append(compose_line(5))
    return haiku


async def generate_haiku_in_background():
    """ Generate haikus in the background and push them to Redis if space is available. """
    while True:
        # Check the current queue size
        current_queue_size = redis_client.llen('haiku_queue')

        if current_queue_size < MAX_QUEUE_SIZE:
            # If the queue size is less than 100, generate a new haiku and push it to the queue
            new_haiku = compose_haiku()
            # Store haiku as JSON string in Redis
            redis_client.rpush('haiku_queue', json.dumps(new_haiku))
            print(f"Pushed new haiku to queue. Current queue size: {current_queue_size + 1}")
        else:
            # If the queue is full, wait for a while before checking again
            print(f"Queue is full with {current_queue_size} haikus. Waiting...")
        await asyncio.sleep(2)  # Sleep for a second before checking again


@app.on_event("startup")
async def startup():
    # Trigger the background task to keep generating haikus
    redis_client.delete('haiku_queue')
    asyncio.create_task(generate_haiku_in_background())


@app.get("/haiku", response_model=HaikuResponse)
async def haiku(number: int):
    haiku_list = []
    while len(haiku_list) < number:
        haiku = redis_client.lpop('haiku_queue')
        if haiku:
            haiku = json.loads(haiku)  # Deserialize JSON string back into list
            haiku_list.append(Haiku(line1=haiku[0], line2=haiku[1], line3=haiku[2]))
        else:
            await asyncio.sleep(1)
    return HaikuResponse(haiku_list=haiku_list)


class ClearQueueResponse(BaseModel):
    success: bool


@app.delete("/haiku")
def clear_queue():
    redis_client.delete('haiku_queue')
    return ClearQueueResponse(success=True)


@app.get("/haiku/qsize")
def queue_size():
    return {"size": redis_client.llen('haiku_queue')}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
