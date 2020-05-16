

async def bell(self):
    return
    await self.wait_until_ready()
    server0 = client.get_guild(694184620811485284)
    server1 = client.get_guild(696207735590486086)
    while True:
        await asyncio.sleep(1)
        t = time.localtime()
        if 0 <= t.tm_wday <= 4 and t.tm_sec in [0, 1]:
            if [t.tm_hour, t.tm_min] in [[8, 0], [8, 25], [9, 0], [9, 10], [9, 15], [10, 15], [10, 25], [10, 30], [11, 30], [12, 25], [12, 30], [13, 30], [13, 40], [13, 45], [14, 45]]:
                for channel in server0.voice_channels + server1.voice_channels:
                    if channel.members:
                        try:
                            await self.youtube(channel, 'bell')
                            print(channel, end=': ')
                            print(t.tm_hour, t.tm_min)
                        except:
                            print(channel)
                            print(channel.members)