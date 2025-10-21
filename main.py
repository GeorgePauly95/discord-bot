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

def blep(body):
    data = body["data"]
    user_input = data["options"]
    animal = user_input[0]["value"]
    small_size = user_input[1]["value"]
    if animal == "animal_dog":
        content = "bow bow!"
    elif animal == "animal_cat":
        content = "meow meow"
    elif animal == "animal_penguin":
        content = "chirp chirp"
    if small_size == True:
        return {"type": 4,
                "data": {
                    "content": content
                    }
                }
    return {
        "type": 4,
        "data": {
            "content": content.upper()
            }
        }

def register_devhud(body):
    print(body)
    return {"type": 4,
            "data": {
                "content": "Your Dev Huddle has been registered!"
                }
            }
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
    print(f"Body is:\n{body}")
    if not verify_signature(signature, timestamp, body):
        raise HTTPException(status_code=401,detail="Invalid signature")
    json_body = json.loads(body)
    return assign_command(json_body)
