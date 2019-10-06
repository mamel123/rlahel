import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("No.1 CHANCE TEAM")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.is_private and message.author.id != "611942063424012324":
        await client.send_message(client.get_channel("630341534436556800"), message.author.name + "(" + message.author.id + ") : " + message.content)
    if message.content.startswith("hacks status"):
        await message.channel.send("FUSE: refurbishment"
                                   "\nD3SK1NG: offline"
                                   "\nATS: online")
    if message.content.startswith("핵 현황"):
        await message.channel.send("FUSE: refurbishment"
                                   "\nD3SK1NG: offline"
                                   "\nATS: online")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
