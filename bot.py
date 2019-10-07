import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("Test")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("hacks status"):
        await message.channel.send("FUSE: offline"
                                   "\nD3SK1NG: online"
                                   "\nATS: online")

    if message.content.startswith("핵 현황"):
        await message.channel.send("FUSE: offline"
                                   "\nD3SK1NG: online"
                                   "\nATS: online")

    if message.content.startswith("데스킹 현황"):
        await message.channel.send("D3SK1NG: online")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
