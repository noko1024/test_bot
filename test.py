#coding UTF-8

import discord
import json
from  watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer

token = json.load(open('./option.json','r'))["token"]
client = discord.Client()
reply_db = None


def on_modified(__):
    global reply_db
    with open('./bot_db.json') as f:
        reply_db = json.load(f)

event_handler = PatternMatchingEventHandler()
event_handler.on_modified = on_modified
    
observer = Observer()
observer.schedule(event_handler, './bot_db.json', recursive=True)
observer.start()


@client.event
async def on_ready():
    print("setup succssfully")
    print("welcome to testbot")
    print("---------------------------")

@client.event
async def on_message(message):
    prefix = "%"

    if message.content.startswith(prefix):
        receive_ms = message.content
        reply = reply_db.get(receive_ms[len(prefix):])
        if reply is None:
            reply = "未登録" #もしdbにkeyが存在しなかったときに返す言葉
        await message.channel.send(reply)
        print("send succses:" + reply)

client.run(token)
