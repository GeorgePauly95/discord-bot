import json
import os
from pydantic import BaseModel
from fastapi import FastAPI, Request, HTTPException
from dotenv import load_dotenv
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError

load_dotenv()

PUBLIC_KEY = os.getenv("PUBLIC_KEY")
verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))


def verify_signature(signature, timestamp, body):
    try:
        verify_key.verify(f"{timestamp}{body}".encode(), bytes.fromhex(signature))
        return True
    except BadSignatureError:
        return False

def acknowledge_ping(body):
    json_body = json.loads(body)
    if json_body["type"] == 1:
        return {"type": 1}
    return "Not PING!"

app = FastAPI()

@app.post("/interactions")
async def root(request: Request):
    headers = request.headers
    signature = headers.get("X-Signature-Ed25519")
    timestamp = headers.get("X-Signature-Timestamp")
    body = await request.body()
    body = body.decode()
    print(f"Body is:\n{body}")
    if not verify_signature(signature, timestamp, body):
        raise HTTPException(status_code=401,detail="Invalid signature")
    return acknowledge_ping(body)
