# https://discordapp.com/api/oauth2/authorize?client_id=687586931844186146&permissions=461824&scope=bot
import discord
import requests

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        await client.change_presence(activity=discord.Game(name="CrazyFuction"))
    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == '!ping':
            await message.channel.send('Hello World! Lets play Ping Pong!')
            print(str(message.author) + " used command !ping at " + str(message.channel))
            print(type(message))
        if message.content == '!meal':
            await message.channel.send('@' + str(message.author).split("#", 1)[0] + " : Your Meal")
            await message.channel.send(":shallow_pan_of_food: :shallow_pan_of_food:")
            print(str(message.author) + " used command !meal at " + str(message.channel))
        if message.content == '!mealall':
            await message.channel.send(str(message.author).split("#", 1)[0] + " sended meals to @everyone :")
            await message.channel.send(":shallow_pan_of_food: :shallow_pan_of_food: :shallow_pan_of_food: :shallow_pan_of_food:")
            print(str(message.author) + " used command !mealall at " + str(message.channel))
        if message.content == '!help':
            embed_help = discord.Embed(title="CrazyFunction Bot Help",description="Help! Help! Help Me!", color=0xffdab9)
            embed_help.add_field(name="List for commands:", value=str(open("help.md").read()), inline=False)
            await message.channel.send(embed=embed_help)
            print(str(message.author) + " used command !help at " + str(message.channel))
        if message.content == '!clear':
            await message.channel.send("start\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\ndone")
            print(str(message.author) + " used command !clear at " + str(message.channel))
        if message.content == '!canmeal':
            await message.channel.send('@' + str(message.author).split("#", 1)[0] + " : Your can food")
            await message.channel.send(":canned_food:﻿ :canned_food:﻿")
            print(str(message.author) + " used command !canmeal at " + str(message.channel))
        if message.content == '!canmeal -all':
            await message.channel.send(str(message.author).split("#", 1)[0] + " sended some can food to @everyone :")
            await message.channel.send(":canned_food:﻿ :canned_food:﻿ :canned_food:﻿ :canned_food:﻿")
            print(str(message.author) + " used command !canmeal (To everyone) at " + str(message.channel))
        if message.content == '!fastfood':
            await message.channel.send('@' + str(message.author).split("#", 1)[0] + " : Your fast food:")
            await message.channel.send(":hamburger: :hamburger:")
            print(str(message.author) + " used command !fastfood at " + str(message.channel))
        if message.content == '!fastfood -all':
            await message.channel.send(str(message.author).split("#", 1)[0] + " sended fsat foods to @everyone :")
            await message.channel.send(":hamburger: :hamburger: :hamburger: :hamburger:")
            print(str(message.author) + " used command !fastfood (To everyone) at " + str(message.channel))
        if message.content == '!info':
            embed_info = discord.Embed(title="CrazyFunction Bot Info", color=0xffdab9)
            embed_info.add_field(name="Designed By: ", value="Emojidiscord#9021", inline=True)
            embed_info.add_field(name="Version: ", value="alpha 2.0", inline=True)
            await message.channel.send(embed=embed_info)
            print(str(message.author) + " used command !info at " + str(message.channel))
        if message.content.find("@!687586931844186146") != -1:
            await message.channel.send("@" + str(message.author).split("#", 1)[0] + ", did you call me?")
            print(str(message.author).split("#", 1)[0] + " called me!")

client = MyClient()
client.run('ID')
print()

