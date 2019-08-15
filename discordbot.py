from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def makia(ctx):
    await ctx.send('https://twitter.com/makia_ymgc')

@bot.command()
async def maro(ctx):
    await ctx.send('https://twitter.com/Marron_castana')
    
@bot.command()
async def cotton(ctx):
    await ctx.send('https://twitter.com/cotton_alta_')
    
@bot.command()
async def botton(ctx):
    await ctx.send('benjoo')
    
bot.run(token)
