from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import toml

config = toml.load("./config.toml")

api_id = config["telegram"]["api_id"]
api_hash = config["telegram"]["api_hash"]

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print()
    print(client.session.save())