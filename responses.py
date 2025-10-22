from pymongo import MongoClient
uri = "mongodb://localhost:27017/"
client = MongoClient(uri)
db = client.bot
dev_huddles = db.dev_huddle

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
    data = body["data"]
    dev_huddle = data["options"]
    dev_huddle_document = {dev_huddle[i]["name"]:dev_huddle[i]["value"] for i in range(len(dev_huddle))}
    dev_huddles.insert_one(dev_huddle_document)
    return {"type": 4,
            "data": {
                "content": f"@{dev_huddle[0]["value"]} - Your Dev Huddle has been registered!"
                }
            }
