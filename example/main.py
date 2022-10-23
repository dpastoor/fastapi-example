from fastapi import FastAPI
import time
import threading
import logging
import uuid
app = FastAPI()

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
log.addHandler(ch)

log.info("starting up")
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/sync")
def fsync():
    request_id = uuid.uuid4()
    thread_id = threading.get_ident()
    log.debug("%s - start of fast_sync",request_id)
    start_time = time.time()
    time.sleep(2)
    log.debug("%s about to return fast_sync", request_id)
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
    log.debug("%s - start of fast_async",request_id)
    start_time = time.time()
    time.sleep(2)
    log.debug("%s about to return fast_async", request_id)
    return {
        "start_time": start_time,
        "send_time": time.time(),
        "thread": thread_id,
        "request_id" : request_id
        }