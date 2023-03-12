import discord
import asyncio

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# @client.event
# async def on_message(message):
#     if message.content.startswith('$thumb'):
#         channel = message.channel
#         await channel.send('Send me that 👍 reaction, mate')

#         def check(reaction, user):
#             return user == message.author and str(reaction.emoji) == '👍'

#         try:
#             reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
#         except asyncio.TimeoutError:
#             await channel.send('👎')
#         else:
#             await channel.send('👍')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '$hello':
        await message.channel.send('Hello!')
    
    if message.content == '$daily-activity':
        await message.channel.send('Please choose the hat you want to contribute to (send the number):\n1. Kindness\n2. Fun')

        def check(m, m_user):
           return m.channel == message.channel and m_user == message.author and m.content == '1'

        try:
           msg, m_user = await client.wait_for('message', timeout=30.0, check=check)
        except asyncio.TimeoutError:
           await message.channel.send('The channel is closed due to inactivity. Please restart by sending \'$daily-activity\'')
        else:
           await message.channel.send('You have choose the Kindness hat!\nPlease input the message below:')

           def k_message(km, k_user):
               return km.channel == message.channel and k_user == message.author
           
           try:
               k_msg, k_user = await client.wait_for('message', timeout=30.0, check=k_message)
           except asyncio.TimeoutError:
               await message.channel.send('The channel is closed due to inactivity.')
           else:
               await message.channel.send('Success!')
    else:
        await message.channel.send('Welcome to That Hat!\nTo start daily-activity, send \'$daily-activity\'')
        return

client.run("MTA4MzI0MjE2OTg1MjI0NDEyMQ.GmBfs1.6LIeM23ReqpJBpv9fdzGb0lxXnIkYoRhKV5RGU")