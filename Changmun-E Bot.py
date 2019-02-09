import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
print("Logged In")
print(client.user.name)
print(client.user.id)
print("--------------------")
await client.change_presence(game=discord.Game(name='디스코드 봇 대화', type=1))

@client.event
async def on_message(message):
if message.content.startswith('.안녕'):
await client.send_message(message.channel, "안녕하세요! '.도움'을 쳐서 명령어를 알아보세요!")

client.run('NTAwNTIzOTA5NTAyOTkyMzk1.D0ARFA.f9P0mEI7pk4u1cawQIbV4u9Tz7Q')
