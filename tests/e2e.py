from telethon import TelegramClient, events, sync
from telethon.sessions import StringSession

import toml, asyncio

config = toml.load("./config.toml")

api_id = config["telegram"]["api_id"]
api_hash = config["telegram"]["api_hash"]
session_name = config["telegram"]["session_name"]
auth_string = config["telegram"]["auth_string"]


loop = asyncio.get_event_loop()

async def send_message_check_reply(conv, text, reply):
    await conv.send_message(text)
    msg = await conv.get_response()
    if not reply in msg.text:
        print('Error: "{}" not found in "{}"'.format(reply, msg.text))
        raise AssertionError
    await asyncio.sleep(1)
    return msg

async def main():
    async with TelegramClient(StringSession(auth_string), api_id, api_hash) as client:

        me = await client.get_me()
        first_name = me.first_name

        async with client.conversation(config["telegram"]["bot_under_test"]) as conv:
            await send_message_check_reply(conv, '/start', "Hello " + first_name + "!\n\nYou just /eat_what_leh and anyhowly uncle will recommend you something to makan lo.")
            await send_message_check_reply(conv, 'a', "No time to chat you leh.. Only /eat_what_leh can work.")
            await send_message_check_reply(conv, '/feedback', "Uncle not ready to accept feedback")


if __name__ == '__main__':
    import logging

    logging.basicConfig(level=logging.INFO)

    loop.run_until_complete(main())