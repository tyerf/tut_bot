import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='~')

@bot.event 
async def on_ready():
    print("}} Bot is online {{")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(877462805954052116)
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(877462805954052116)
    await channel.send(f'{member} leave')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')

bot.run('ODc3Mzc0NjA3ODQ4NTM0MDM2.YRxsxw.DHS3VD-Dr6uasncyvIHI7MuvOYM')