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

    if message.content.startswith("!핵 현황"):
        await message.channel.send("FUSE: offline"
                                   "\nD3SK1NG: online"
                                   "\nATS: online")

    if message.content.startswith("데스킹 현황"):
        await message.channel.send("D3SK1NG: online")
        
    if message.content.startswith("!뉴스 현황"):
        await message.channel.send("현재 새로운 뉴스가 있습니다.")
    
    if message.content.startswith("!명령어"):
        await message.channel.send("```ini"
                                   "\n[ 명령어 ]```"
                                   "\n```fix"
                                   "\n!핵 현황"
                                   "\n!뉴스 현황"
                                   "\n!news
                                   "\n!fivem```")

        if message.content.startswith("!fivem"):
        await message.channel.send("```fix"
                                   "\n※ 안녕하세요 CHANCE 서버 입니다.```**"
                                   "\n───────────────────────────────────────────────────"
                                   "\n**```md"
                                   "\n 1 : 서버 오픈 준비는 많이 걸렸지만 서버 운영과 유저분들의 즐거움을 위한 서버입니다!"
                                   "\n 2 : 서버 내 불편, 건의, 개선사항을 관리자에게 말씀해주시면 빠른 답변과 업데이트로 플레이하는데 차질없게 하겠습니다!"
                                   "\n 3 : 유저분들의 즐거운 RP를 위하여 유저를 먼저 생각하는 친절한 관리자들과 친절한 유저들! 함께 서버를 만들어갑시다!"
                                   "\n 4 : 새로오신 뉴비분들도 불편함 없게 뉴비교육을 실시하고 있습니다!```**"
                                   "\n───────────────────────────────────────────────────"
                                   "\n**```yaml"
                                   "\n《[신생] KR RP CHANCE SERVER》"
                                   "\n☆ Server Name :  KR RP CHANCE SERVER ```**"
                                   "\n───────────────────────────────────────────────────"
                                   "\n**```tex"
                                   "\n$ 배달부, 택시 , 정비공, 어부 등등 다양한 직업들이 있습니다!"

                                   "\n지나가시던 분들도 한번 오셔서 부족한점 건의해주시면 더 쾌적한 서버를 만들도록 노력하겠습니다. 감사합니다 !```"
                                   "\n───────────────────────────────────────────────────"
                                   "\n```css"
                                   "\n『 디스코드 주소 』"
                                   "\n※ 디스코드 참여 : https://discord.gg/9CWjZpr"
                                   "\n※ 입국방법은 디스코드 접속 후 시민 인증 신청```"
                                   "\n@everyone")

    if message.content.startswith("!news"):
        await message.channel.send("__**The developer is on vacation, so it takes a while for the FUSE re-release.**__")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
