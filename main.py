import discord
import asyncio
import

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
    
    if message.content == '$write':
        await message.channel.send('Please choose the hat you want to contribute to:\n1. Kindness\n2. Fun')

        def check(m):
           return m.channel == message.channel and m.content == 'Kindness'

        try:
           msg = await client.wait_for('message', timeout=30.0, check=check)
        except asyncio.TimeoutError:
           await message.channel.send('The channel closed due to inactivity.')
        else:
           await message.channel.send('You have choose the Kindness hat!\nPlease input the message below:')

responses = {}
for i in range(2):
    username = input("Enter your username: ")
    user_response = input("Enter your response: ")
    thisdict = {username.title():user_response}
    responses.update(thisdict)

client.run("MTA4MzI0MjE2OTg1MjI0NDEyMQ.GmBfs1.6LIeM23ReqpJBpv9fdzGb0lxXnIkYoRhKV5RGU")
