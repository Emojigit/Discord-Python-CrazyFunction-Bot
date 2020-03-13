# https://discordapp.com/api/oauth2/authorize?client_id=687586931844186146&permissions=461824&scope=bot
import discord
import requests

count = requests.get('http://gamers-control-2.000webhostapp.com/count.txt')


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == '!ping':
            await message.channel.send('Hello World! Lets play Ping Pong!')
        if message.content == '!meal':
            await message.channel.send('@' + str(message.author).split("#", 1)[0] + " : Your Meal")
            await message.channel.send(":shallow_pan_of_food: :shallow_pan_of_food:")
        if message.content == '!mealall':
            await message.channel.send(str(message.author).split("#", 1)[0] + " sended meals to @everyone :")
            await message.channel.send(":shallow_pan_of_food: :shallow_pan_of_food: :shallow_pan_of_food: :shallow_pan_of_food:")
        if message.content == '!help':
            await message.channel.send(open("help.md").read())
        if message.content == '!clear':
            await message.channel.send("start\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\ndone")
        if message.content == '!canmeal':
            await message.channel.send('@' + str(message.author).split("#", 1)[0] + " : Your can food")
            await message.channel.send(":canned_food:﻿ :canned_food:﻿")
        if message.content == '!canmeal -all':
            await message.channel.send(str(message.author).split("#", 1)[0] + " sended some can food to @everyone :")
            await message.channel.send(":canned_food:﻿ :canned_food:﻿ :canned_food:﻿ :canned_food:﻿")
        if message.content == '!info':
            await message.channel.send(str(open("info.md").read()))

client = MyClient()
client.run('MY-TOKEN')
print()


