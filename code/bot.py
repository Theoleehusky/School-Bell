import discord
import re
import requests
import time
import asyncio
from bs4 import BeautifulSoup
import os
import json

path = os.getcwd()


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.bg_task = self.loop.create_task(self.my_background_task())

    async def on_ready(self):
        print('Logged in as', self.user.name)
        await client.change_presence(activity=discord.Activity(name='you', type=discord.ActivityType.watching))

    async def on_message(self, message):
        # if message.content == "stop":
        #     try:
        #
        #     except:
        #         print("No channel")
        message.content = ' ' + message.content + ' '

        if message.author == client.user:
            return
        message.content = message.content.lower()

        if re.search("stfu|shut up|bitch|whore|retard|cunt", message.content):
            await message.channel.send("D:")
        if re.search("@everyone|@here|@sas|@juniors|@seniors", message.content):
            await message.channel.send("woah mass ping")
        if re.search(" no you | no u ", message.content):
            await message.channel.send("no u")
        if re.search("schedule", message.content):
            await message.channel.send(file=discord.File('references/schedule.png'))
        if re.search(" ap ", message.content):
            await message.channel.send(file=discord.File('AP.jpg'))
        if re.search("what day", message.content):
            await message.channel.send('Today: ' + dictionary[time.localtime().tm_yday] + '     Tomorrow: ' + dictionary[time.localtime().tm_yday+1])
        if re.search("covid|corona|wuhan|virus", message.content):
            await message.channel.send("Coronavirus cases: " + corona())
        if message.content == " khan ":
            await self.youtube(message.author.voice.channel, 'khan')
        if message.content == " school bell ":
            await self.youtube(message.author.voice.channel, 'bell')

    async def my_background_task(self):

    async def youtube(self, channel, key):
        voice = await channel.connect()
        if key == "bell":
            voice.play(discord.FFmpegPCMAudio('bell.mp3'))
        elif key == "khan":
            voice.play(discord.FFmpegPCMAudio('khan.mp3'))
        time.sleep(1)
        while voice.is_playing():
            await asyncio.sleep(1)
        await voice.disconnect()


URL = 'https://www.worldometers.info/coronavirus/'


def corona():
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(style="color:#aaa")
    return results.string.split(">")[0]


dictionary = {}
arr = ['A', 'B', 'C', 'D']
n = 0
for day in range(104, 367):
    if day in [122, 128, 146]:
        dictionary[day] = "Holiday"
    elif day % 7 == 4:
        dictionary[day] = "Saturday"
    elif day % 7 == 5:
        dictionary[day] = "Sunday"
    else:
        dictionary[day] = arr[n] + ' Day'
        n += 1
        n = n % 4


with open(os.path.join(path, 'code/references/token.txt'), 'r') as f:
    token = json.load(f)

client = MyClient()
client.run(token)

