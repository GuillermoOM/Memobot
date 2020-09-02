# Work with Python 3.6
#Discord Bot!

import discord
from discord.ext import commands
import random, aiohttp, json, asyncio

BOT_PREFIX = ("?")
TOKEN = ""

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix=BOT_PREFIX, description=description)

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="?h for commands!"))
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.remove_command('help')

@bot.command()
async def h(ctx):
    embed = discord.Embed(title="Comandos de Memobot", description="Usar prefijo '?'", color=0x2E4172)
    embed.add_field(name="Comandos Generales", value="?info \n ?bticoin \n ?h")
    await ctx.send(embed=embed)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Memobot", description="Un experimento casual", color=0x2E4172)
    
    # give info about you here
    embed.add_field(name="Author", value="willywolfy")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="[Invite link](https://discordapp.com/api/oauth2/authorize?client_id=491654144004849705&permissions=0&scope=bot)")

    await ctx.send(embed=embed)

@bot.command()
async def bitcoin(ctx):
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await ctx.send("Bitcoin price is: $" + response['bpi']['USD']['rate'])

bot.run(TOKEN)