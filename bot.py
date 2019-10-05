import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("No.1 CHANCE TEAM")
    await client.change_presence(status=discord.Status.offline, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("hacks status"):
        await message.channel.send("FUSE: refurbishment"
                                   "\nD3SK1NG: offline"
                                   "\nATS: online")
    if message.content.startswith("핵 현황"):
        await message.channel.send("FUSE: refurbishment"
                                   "\nD3SK1NG: offline"
                                   "\nATS: online")


client.run("NjExOTQyMDYzNDI0MDEyMzI0.XZkbYQ.pfNxK_gXPFcShX5_HG3BXNkgPZo")