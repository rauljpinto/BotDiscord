import discord
import random
import os
from keepalive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
    print('{0.user} pronto para o serviço'.format(client))
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!d'):
      user = message.author.mention
      if "+" in message.content:
        txt = message.content
        lados, num = txt.split('+')
        mod = int(num)
        lados_num = lados.replace("!d", "")
        d = int(lados_num)
        roll = random.randint(1, d)
        total = roll + mod
        await message.channel.send(f'{user}\n **Resultado:** {roll}\n **Total:** {total}')
      if "-" in message.content:
        txt = message.content
        lados, num = txt.split('-')
        mod = int(num)
        lados_num = lados.replace("!d", "")
        d = int(lados_num)
        roll = random.randint(1, d)
        total = roll - mod
        await message.channel.send(f'{user}\n **Resultado:** {roll}\n **Total:** {total}')
      else:
        txt = message.content
        lados_num = txt.replace("!d", "")
        d = int(lados_num)
        roll = random.randint(1, d)
        await message.channel.send(f'{user}\n **Resultado:** {roll}\n **Total:** {roll}')


keep_alive()        
client.run(os.environ['t0ken'])