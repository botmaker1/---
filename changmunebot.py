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

@client.event
async def on_message(message):
    if message.content.startswith('.도움'):
        await client.send_message(message.channel, "창문이-봇의 도움말입니다! 모든 명령어에는 온점(.)을 붙여주세요! 1. 4딸라  2. 글카")  
    if message.content.startswith('안녕'):
        await client.send_message(message.channel, "안 녕 하 세 요! 창문이-봇입니다! '.도움'을 쳐서 명령어를 알아보세요!")
    if message.content.startswith('.4딸라'):
        await client.send_message(message.channel, "오케이, 땡큐, 오케이, __**``4딸라!``**__ (https://m.youtube.com/watch?v=YPcSzJaaKho&t=214s)-이건 4딸라 영상입니다.")
    if message.content.startswith('.글카'):
        await client.send_message(message.channel, "가성비를 원하시면 엔비디아 대신 에이엠디로 가시는 걸 추천합니다.")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
