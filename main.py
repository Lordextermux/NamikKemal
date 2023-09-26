import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def join(ctx):
    # Botun belirli bir ses kanalına katılma komutu
    voice_channel = ctx.author.voice.channel
    await voice_channel.connect()

@bot.command()
async def leave(ctx):
    # Botun ses kanalından ayrılma komutu
    voice_client = ctx.voice_client
    await voice_client.disconnect()

bot.run('YOUR_TOKEN_HERE')
