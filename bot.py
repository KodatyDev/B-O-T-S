import os
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logado como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "!ping":
        await message.channel.send("Pong 🏓")

# pega o token do secret do GitHub
TOKEN = os.getenv("DISCORD_TOKEN")
client.run(TOKEN)