import requests
import os
from dotenv import load_dotenv
from commands import dev_huddle

load_dotenv()

APP_ID = os.getenv("APP_ID")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# url = f"https://discord.com/api/v10/applications/{APP_ID}/commands"
url = f"https://discord.com/api/v10/applications/{APP_ID}/commands/1429783353674170498"

# For authorization, you can use either your bot token
headers = {
    "Authorization": f"Bot {BOT_TOKEN}"
}

r = requests.patch(url, headers=headers, json=dev_huddle)
