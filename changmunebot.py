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
    if message.content.startswith(".안녕"):
        await client.send_message(message.channel, "안녕하세요! '.도움'을 쳐서 명령어를 알아보세요!")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
