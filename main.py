import discord
import os

client= discord.Client()
      
@client.event
async.def on_ready():
      print("SnowBot is now online.")
      print(client.user)

@client.event
async def on_message(message):
      if message.author != client.user:
            await client.send_message(message.content[::-1])
        
token = os.environ.get(DISCORD_BOT_SECRET")
client.run(token)
