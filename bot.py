import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(intents=intents, command_prefix="?", case_sensitive=False)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# Run bot with predefined token
with open("tokens/discord") as botToken:
    client.run(botToken.readline())