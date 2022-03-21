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
    reply_db = open('./bot_db.json','r')
    prefix = "$"

    if message.content.startswith(prefix):
        receive_ms = message.content
        #key = receive_ms.replace(prefix,'')
        reply = json.load(reply_db)[receive_ms.replace(prefix,'')]
        await message.channel.send(reply)
        print("send succses:" + reply)

client.run(token)
