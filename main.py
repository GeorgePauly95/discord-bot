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

app = FastAPI()

@app.post("/interactions")
def interactions(request: Request):
    headers = request.headers
    signature = headers.get("X-Signature-Ed25519")
    timestamp = headers.get("X-Signature-Timestamp")
    body = request.body().decode()
    # Did not include the above 4 lines in verify_signature function, 
    # since they will be used for other purposes. 
    if not verify_signature(signature, timestamp, body):
        raise HTTPException(status_code=401,detail="Invalid signature")
    acknowledge_ping(body)


