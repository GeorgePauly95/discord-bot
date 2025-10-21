import requests
import os
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("APP_ID")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# url = f"https://discord.com/api/v10/applications/{APP_ID}/commands"
url = f"https://discord.com/api/v10/applications/{APP_ID}/commands/1429783353674170498"

dev_huddle = {
    "name": "register_devhud",
    "type": 1,
    "description": "Register a dev huddle",
    "options": [
        {
            "name": "name",
            "description": "Name of the person giving the dev huddle",
            "type": 6,
            "required": True,
        },
        {
            "name": "date",
            "description": "Provide date of the dev huddle in dd-mm-yy format please",
            "type": 3,
            "required": True,
        },
        {
            "name": "topic",
            "description": "The topic of the dev huddle",
            "type": 3,
            "required": True,
        },
        {
            "name": "description",
            "description": "A short description of the dev huddle",
            "type": 3,
            "required": True,
        }
    ]
}

# sample_command = {
#     "name": "blep",
#     "type": 1,
#     "description": "Send a random adorable animal photo",
#     "options": [
#         {
#             "name": "animal",
#             "description": "The type of animal",
#             "type": 3,
#             "required": True,
#             "choices": [
#                 {
#                     "name": "Dog",
#                     "value": "animal_dog"
#                 },
#                 {
#                     "name": "Cat",
#                     "value": "animal_cat"
#                 },
#                 {
#                     "name": "Penguin",
#                     "value": "animal_penguin"
#                 }
#             ]
#         },
#         {
#             "name": "only_smol",
#             "description": "Whether to show only baby animals",
#             "type": 5,
#             "required": False
#         }
#     ]
# }



# For authorization, you can use either your bot token
headers = {
    "Authorization": f"Bot {BOT_TOKEN}"
}

# r = requests.post(url, headers=headers, json=dev_huddle)
r = requests.patch(url, headers=headers, json=dev_huddle)
print(r, r.text, r.headers)
