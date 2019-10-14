import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("!news")
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
        
    if message.content.startswith("뉴스 현황"):
        await message.channel.send("현재 새로운 뉴스가 있습니다.)

    if message.content.startswith("!news"):
        await message.channel.send("__**The developer is on vacation, so it takes a while for the FUSE re-release.**__")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
