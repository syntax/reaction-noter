import discord
from discord.ext import commands

client = discord.Client()
client = commands.Bot(command_prefix='.')


#add blacklisted emoji ids in here x
bademojis = ['','']
logchannelid = ''
apikey = ''

@client.event
async def on_raw_reaction_add(reaction):
    rudeuser = reaction.user_id
    if reaction.event_type == 'REACTION_ADD':
        if reaction.emoji in bademojis:
            embed = discord.Embed(title='Found a dickhead',
                                description=f"{rudeuser.mention} just added a blacklisted reaction:\n\n<:_:{reaction.emoji}>\n\nin <#{reaction.channel_id}>",
                                colour=0x000000)

            embed.set_footer(text="@syntaxszn • made with love")
            logchannel = client.get_channel(logchannelid)
            await logchannel.send(embed=embed)


client.run()
