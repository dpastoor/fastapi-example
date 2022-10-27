from fastapi import FastAPI
import time
import threading
import logging
import uuid
import os
import asyncio
app = FastAPI()

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
# lets log to console with a decent format
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
log.addHandler(ch)

log.info("starting up")
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/sync")
def fsync():
    request_id = uuid.uuid4()
    thread_id = threading.get_ident()
    log.debug("%s - start of sync on thread %s",request_id, thread_id)
    start_time = time.time()
    log.debug("%s about to return sync on thread %s, process_id: %s", request_id, thread_id, os.getpid())
    return {
        "start_time": start_time,
        "send_time": time.time(),
        "thread": thread_id,
        "request_id" : request_id
        }

@app.get("/async")
async def fasync():
    request_id = uuid.uuid4()
    thread_id = threading.get_ident()
    log.debug("%s - start of async on thread %s",request_id, thread_id)
    start_time = time.time()
    await asyncio.sleep(1)
    log.debug("%s about to return async on thread %s, process_id: %s", request_id, thread_id, os.getpid())
    return {
        "start_time": start_time,
        "send_time": time.time(),
        "thread": thread_id,
        "request_id" : request_id
        }