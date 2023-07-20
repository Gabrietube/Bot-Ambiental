import discord
import random
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')

@bot.command()
async def lista(ctx):
    await ctx.send("""Acciones para cuidar el medio ambiente: 
    -No uses bolsas plasticas 
    -Ahorra el agua 
    -Separa los residuos 
    -Recicla 
    -Apaga las luces 
    -Utiliza bombillas de bajo consumo""")

@bot.command()
async def afiche(ctx):
        img_name = random.choice(os.listdir('images'))
        with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)

bot.run("TOKEN")
