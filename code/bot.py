import discord
import re
import time
import asyncio
from corona import corona


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
            await message.channel.send(file=discord.File('references/AP.jpg'))
        if re.search("what day", message.content):
            await message.channel.send('Today: ' + dictionary[time.localtime().tm_yday] + '     Tomorrow: ' + dictionary[time.localtime().tm_yday+1])
        if re.search("covid|corona|wuhan|virus", message.content):
            await message.channel.send("Coronavirus cases: " + corona())
        if message.content == " khan ":
            await youtube(message.author.voice.channel, 'khan')
        if message.content == " school bell ":
            await youtube(message.author.voice.channel, 'bell')

    async def my_background_task(self):
        await self.wait_until_ready()
        server0 = client.get_guild(694184620811485284)
        server1 = client.get_guild(696207735590486086)
        while True:
            await asyncio.sleep(1)
            t = time.localtime()
            if 0 <= t.tm_wday <= 4 and t.tm_sec in [0, 1]:
                if [t.tm_hour, t.tm_min] in [[8, 0], [8, 25], [9, 0], [9, 10], [9, 15], [10, 15], [10, 25], [10, 30],
                                             [11, 30], [12, 25], [12, 30], [13, 30], [13, 40], [13, 45], [14, 45]]:
                    for channel in server0.voice_channels + server1.voice_channels:
                        if channel.members:
                            try:
                                await youtube(channel, 'bell')
                                print(channel, end=': ')
                                print(t.tm_hour, t.tm_min)
                            except:
                                print(channel)
                                print(channel.members)


async def youtube(channel, key):
    voice = await channel.connect()
    if key == "bell":
        voice.play(discord.FFmpegPCMAudio('references/bell.mp3'))
    elif key == "khan":
        voice.play(discord.FFmpegPCMAudio('references/khan.mp3'))
    time.sleep(1)
    while voice.is_playing():
        await asyncio.sleep(1)
    await voice.disconnect()


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


with open('references/token.txt', 'r') as f:
    token = f.read()
client = MyClient()
client.run(token)
