#coding UTF-8

import discord
import json

token = json.load(open('./option.json','r'))["token"]
client = discord.Client()

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
        with open('./bot_db.json') as reply_db:
            reply = json.load(reply_db)[receive_ms.replace(prefix,'')]
        await message.channel.send(reply)
        print("send succses:" + reply)

client.run(token)
