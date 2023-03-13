import discord
import asyncio
import random

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

savedKMessage = {}
savedFMessage = {}


# class Save_ID:
#     def __init__(self, message_id, message):
#         self.message_id = message_id
#         self.message = message

#     def __str__(self):
#         return f"{self.message_id}({self.message})"

#     # def myfunc(self):
#     #     print("Hello my name is " + self.message)


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
        await message.channel.send('Welcome to That Hat!\nTo start daily-activity, send \'$daily-activity\'')

    if message.content == '$daily-activity':
        await message.channel.send('Please choose the hat you want to contribute to (send the number):\n1. Kindness\n2. Fun')

        def check(m):
            return m.channel == message.channel and ((m.content == '1') | (m.content == '2')) and m.author == message.author

        try:
            msg = await client.wait_for('message', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await message.channel.send('The channel is closed due to inactivity. Please restart by sending \'$daily-activity\'')
        else:
            if (msg.content == '1'):
                await message.channel.send('You have chosen the Kindness hat!\nGive me your most inspirational quote (5min):')

                def k_message(km):
                    return km.channel == message.channel and km.author == message.author

                try:
                    kmsg = await client.wait_for('message', timeout=300.0, check=k_message)
                except asyncio.TimeoutError:
                    await message.channel.send('The channel is closed due to inactivity. Please restart by sending \'$daily-activity\'')
                else:
                    savedKMessage[kmsg.id] = kmsg
                    await message.channel.send('You have successfully thrown the message into the Kindness hat!\nNow it is time to draw from the Kindness hat.\nIf you like the message you can react to it with a thumbsup (in 60s)\nThe message you draw is:')
                    kmsg_id, kmsg_random = random.choice(
                        list(savedKMessage.items()))
                    # while (kmsg_random.author == message.author):
                    #     kmsg_id, kmsg_random = random.choice(
                    #         list(savedKMessage.items()))
                    # combine = Save_ID(kmsg_id, kmsg_random)
                    await message.channel.send(kmsg_random.content)

                    def k_message_react(reaction, user):
                        return user == message.author and str(reaction.emoji) == '👍' and reaction.message.channel == message.channel

                    try:
                        reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=k_message_react)
                    except asyncio.TimeoutError:
                        await message.channel.send('You have successfully completed the daily activity! Have a great day!')
                    else:
                        await kmsg_random.author.send(f'Someone has liked your message \'{kmsg_random.content}\' in the Kindness hat!')
                        await message.channel.send('The sender of the message will receive your like!\nDo you want to start a conversation with the sender of the message? (send Yes or No in 60s)')

                        def k_start_conversation(ksc):
                            return ksc.channel == message.channel and ((ksc.content == 'Yes') | (ksc.content == 'No')) and ksc.author == message.author

                        try:
                            conversation_kmsg = await client.wait_for('message', timeout=60.0, check=k_start_conversation)
                        except asyncio.TimeoutError:
                            await message.channel.send('You have successfully completed the daily activity! Have a great day!')
                        else:
                            if (conversation_kmsg.content == 'Yes'):
                                await kmsg_random.author.send(f'A person who liked your message \'{kmsg_random.content}\' in the Kindness hat would like to have a conversation with you!\nIf you agree to connect please add {message.author}')
                                await message.channel.send('The message request is sent!\nA reminder: the conversation will only be started if the other people agree to connect.')
                                await message.channel.send('You have successfully completed the daily activity! Have a great day!')
                            else:
                                await message.channel.send('You have successfully completed the daily activity! Have a great day!')
            else:
                await message.channel.send('You have chosen the Fun hat!\nGive me your best pickup line ;D (5min):')

                def f_message(fm):
                    return fm.channel == message.channel and fm.author == message.author

                try:
                    fmsg = await client.wait_for('message', timeout=300.0, check=f_message)
                except asyncio.TimeoutError:
                    await message.channel.send('The channel is closed due to inactivity. Please restart by sending \'$daily-activity\'')
                else:
                    savedFMessage[fmsg.id] = fmsg
                    await message.channel.send('You have successfully thrown the message into the Fun hat!\nNow it is time to draw from the Fun hat.\nIf you like the message you can react to it with a thumbsup (in 60s)\nThe message you draw is:')
                    fmsg_id, fmsg_random = random.choice(
                        list(savedFMessage.items()))
                    # while (fmsg_random.author == message.author):
                    #     fmsg_id, fmsg_random = random.choice(
                    #         list(savedFMessage.items()))
                    # combine = Save_ID(fmsg_id, fmsg_random)
                    await message.channel.send(fmsg_random.content)

                    def f_message_react(reaction, user):
                        return user == message.author and str(reaction.emoji) == '👍' and reaction.message.channel == message.channel

                    try:
                        reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=f_message_react)
                    except asyncio.TimeoutError:
                        await message.channel.send('You have successfully completed the daily activity! Have a great day!')
                    else:
                        await fmsg_random.author.send(f'Someone has liked your message \'{fmsg_random.content}\' in the Fun hat!')
                        await message.channel.send('The sender of the message will receive your like!\nDo you want to start a conversation with the sender of the message? (send Yes or No in 60s)')

                        def f_start_conversation(fsc):
                            return fsc.channel == message.channel and ((fsc.content == 'Yes') | (fsc.content == 'No')) and fsc.author == message.author

                        try:
                            conversation_fmsg = await client.wait_for('message', timeout=60.0, check=f_start_conversation)
                        except asyncio.TimeoutError:
                            await message.channel.send('You have successfully completed the daily activity! Have a great day!')
                        else:
                            if (conversation_fmsg.content == 'Yes'):
                                await fmsg_random.author.send(f'A person who liked your message \'{fmsg_random.content}\' in the Kindness hat would like to have a conversation with you!\nIf you agree to connect please add {message.author}')
                                await message.channel.send('The message request is sent!\nA reminder: the conversation will only be started if the other people agree to connect.')
                                await message.channel.send('You have successfully completed the daily activity! Have a great day!')
                            else:
                                await message.channel.send('You have successfully completed the daily activity! Have a great day!')

client.run(
    "MTA4MzI0MjE2OTg1MjI0NDEyMQ.GmBfs1.6LIeM23ReqpJBpv9fdzGb0lxXnIkYoRhKV5RGU")
