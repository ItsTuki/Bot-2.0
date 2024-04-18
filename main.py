import discord
import os
import random
import requests

print(os.listdir('tukis'))
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')
@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir("tukis"))
    with open(f'tukis/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
bot.run("Token Here")