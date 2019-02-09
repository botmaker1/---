import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("Login")
    print(client.user.name)
    print(client.user.id)
    print("--------------------")
    await client.change_presence(game=discord.Game(name='', type=1))

    if message.content.startswith("안녕"):
        await client.send_message(message.channel, "안녕하세요! 창문이-봇입니다! '.도움'을 쳐서 명령어를 알아보세요!")
    
    if message.content.startswith(".도움"):
        await client.send_message(message.channel, "창문이-봇의 도움말입니다. 모든 명령어 앞에는 온점을 붙여주셔야 합니다! .주사위(이건 .주사위를 타이핑 한 후 띄어쓰기 한 후 아무 숫자나 쓴 뒤 .을 붙여주시고 그 뒤에 또 숫자를 붙여주셔야 합니다. ex).주사위 3.5")               
    
    if message.content.startswith(".주사위"):
        roll = message.content.split(" ")
        rolld = roll[1].split(".")
        dice = 0
        for i in range(1, int(rolld[0])+1):
            dice = dice + random.randint(1, int(rolld[1]))
        await client.send_message(message.channel, str(dice))
                    

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
