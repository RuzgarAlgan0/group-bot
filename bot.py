import discord
from discord.ext import commands
import random
import os
import requests
print(os.listdir("GRAPHS"))
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')


@bot.command()
async def ornekler(ctx):
    url_name = random.choice(os.listdir('graphs'))
    with open(f'graphs/{url_name}', 'rb') as f:
        url = discord.File(f)
 
    await ctx.send(file=url)

bot.run("Token")
