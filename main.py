import json
import os
import pymongo
from pydantic import BaseModel
from fastapi import FastAPI, Request, HTTPException
from dotenv import load_dotenv
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
from commands import blep, register_devhud 
load_dotenv()

PUBLIC_KEY = os.getenv("PUBLIC_KEY")
verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))


def verify_signature(signature, timestamp, body):
    try:
        verify_key.verify(f"{timestamp}{body}".encode(), bytes.fromhex(signature))
        return True
    except BadSignatureError:
        return False

command_directory = {"blep": blep, "register_devhud":register_devhud}

def assign_command(body):
    type = body["type"]
    if type == 1:
        return {"type": 1}
    name = body["data"]["name"]
    return command_directory[name](body)

app = FastAPI()

@app.post("/interactions")
async def root(request: Request):
    headers = request.headers
    signature = headers.get("X-Signature-Ed25519")
    timestamp = headers.get("X-Signature-Timestamp")
    body = await request.body()
    body = body.decode()
    if not verify_signature(signature, timestamp, body):
        raise HTTPException(status_code=401,detail="Invalid signature")
    json_body = json.loads(body)
    return assign_command(json_body)
