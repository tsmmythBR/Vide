import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

@client.event
async def on_ready():
    await client.change_presence(game=Game(name='trekvogels', type = 2))
    print('trekvogel is ready :)')
    
    @client.event
async def on_member_join(member):
    await client.send_message(member, "Welkom bij Marco! Heb een leuke tijd en vergeet zeker niet om een command zoals !janee te proberen of natuurlijk 'help' fijne dag!")
    await client.send_message(member, "-------------------------------------------------------------------")
    await client.send_message(member, "In deze server ben je een trekvogel")
    await client.send_message(member, "Je kan samen trekken met de trekvogels")
    await client.send_message(member, "-------------------------------------------------------------------")
    
    
    @client.event
     if message.content.startswith('!janee'):
        randomlist = ['Ja','Nee']
        await client.send_message(message.channel,(random.choice(randomlist)))
     if message.content.startswith('!vriend'):
        randomlist = ['20%','30%','40%','50%','60%','70%','80%','90%','100%']
        await client.send_message(message.channel,(random.choice(randomlist)))
        
 client.run('HIERJETOKEN')
