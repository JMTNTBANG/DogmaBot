import os
import time
import requests
import threading
import discord
import urllib
from discord.ui import Button, View
import random
from discord import app_commands, member, InteractionMessage
from discord.ext.commands import has_permissions, MissingPermissions
from dotenv import load_dotenv


intents = discord.Intents.default()
intents.members = True

# Load important things

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

async def sendButtonRoles():
    Foodies=Button(label="Food Channels", style=discord.ButtonStyle.gray, emoji="<:frank_pizza:1050272497062387823>")
    MusicEnjoyers=Button(label="Music Channels", style=discord.ButtonStyle.gray, emoji="<:frank_huh_duhs:1057140942630555658>")
    ComicNerds=Button(label="Comic Book Channels", style=discord.ButtonStyle.gray, emoji="<:superhero_frank:1057143128726970509>")
    MovieBingers=Button(label="Movie Channels", style=discord.ButtonStyle.gray, emoji="<:frank_itscorn:1054938744890863666>")
    Artists=Button(label="Art/Creativity Channels", style=discord.ButtonStyle.gray, emoji="<:dominanceIsFrank:1052478307377090591>")
    DMOffers=Button(label="DM Offers", style=discord.ButtonStyle.gray)

# Foodies (1054579102834765924)
    async def FoodiesCallback(button_info):
        role = client.get_guild(1053851544765874216).get_role(1054579102834765924)
        member = client.get_guild(1053851544765874216).get_member(button_info.user.id)

        if role.members.__contains__(member):
            await member.remove_roles(role)
            await button_info.response.send_message("Removed \"Foodies\" Role", ephemeral=True)
        else:
            await member.add_roles(role)
            await button_info.response.send_message("You have been given the \"Foodies\" Role", ephemeral=True)
# Music Enjoyers (1054579691324977235)
    async def MusicEnjoyersCallback(button_info):
        role = client.get_guild(1053851544765874216).get_role(1054579691324977235)
        member = client.get_guild(1053851544765874216).get_member(button_info.user.id)

        if role.members.__contains__(member):
            await member.remove_roles(role)
            await button_info.response.send_message("Removed \"Music Enjoyers\" Role", ephemeral=True)
        else:
            await member.add_roles(role)
            await button_info.response.send_message("You have been given the \"Music Enjoyers\" Role", ephemeral=True)
# Comic Nerds (1054580151163306004)
    async def ComicNerdsCallback(button_info):
        role = client.get_guild(1053851544765874216).get_role(1054580151163306004)
        member = client.get_guild(1053851544765874216).get_member(button_info.user.id)

        if role.members.__contains__(member):
            await member.remove_roles(role)
            await button_info.response.send_message("Removed \"Comic Nerds\" Role", ephemeral=True)
        else:
            await member.add_roles(role)
            await button_info.response.send_message("You have been given the \"Comic Nerds\" Role", ephemeral=True)
# Movie Bingers (1054580799627857951)
    async def MovieBingersCallback(button_info):
        role = client.get_guild(1053851544765874216).get_role(1054580799627857951)
        member = client.get_guild(1053851544765874216).get_member(button_info.user.id)

        if role.members.__contains__(member):
            await member.remove_roles(role)
            await button_info.response.send_message("Removed \"Movie Bingers\" Role", ephemeral=True)
        else:
            await member.add_roles(role)
            await button_info.response.send_message("You have been given the \"Movie Bingers\" Role", ephemeral=True)
# Artists (1054581231674732695)
    async def ArtistsCallback(button_info):
        role = client.get_guild(1053851544765874216).get_role(1054581231674732695)
        member = client.get_guild(1053851544765874216).get_member(button_info.user.id)

        if role.members.__contains__(member):
            await member.remove_roles(role)
            await button_info.response.send_message("Removed \"Artists\" Role", ephemeral=True)
        else:
            await member.add_roles(role)
            await button_info.response.send_message("You have been given the \"Artists\" Role", ephemeral=True)
# DM Offers (1055600368236646471)
    async def DMOffersCallback(button_info):
        role = client.get_guild(1053851544765874216).get_role(1055600368236646471)
        member = client.get_guild(1053851544765874216).get_member(button_info.user.id)

        if role.members.__contains__(member):
            await member.remove_roles(role)
            await button_info.response.send_message("Removed \"DM Offers\" Role", ephemeral=True)
        else:
            await member.add_roles(role)
            await button_info.response.send_message("You have been given the \"DM Offers\" Role", ephemeral=True)

    Foodies.callback=FoodiesCallback
    MusicEnjoyers.callback=MusicEnjoyersCallback
    ComicNerds.callback=ComicNerdsCallback
    MovieBingers.callback=MovieBingersCallback
    Artists.callback=ArtistsCallback
    DMOffers.callback=DMOffersCallback
        
        

    view=View()
    view.add_item(Foodies)
    view.add_item(MusicEnjoyers)
    view.add_item(ComicNerds)
    view.add_item(MovieBingers)
    view.add_item(Artists)
    view.add_item(DMOffers)
    await client.get_channel(1054578163520376862).send('Click this button to sign up for deals and offers directly to your dm', view=view)


# Activate Bot

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=intents,)

    async def on_ready(self):
        await self.wait_until_ready()
        self.synced = False
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild=discord.Object(id=1053851544765874216))
            self.synced=True
            print('Commands Synced')
        print(f'Bot is online')
        # await client.change_presence(activity=discord.Game(name="DEBUG MODE"))
        # print('Bot Presence changed to \"Playing DEBUG MODE\"')
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="live bands"))
        print('Bot Presence changed to \"Listening to live bands\"')

        await client.get_channel(1054578163520376862).purge()
        await sendButtonRoles()

client = aclient()

@client.event
async def on_message(message: discord.Message):
    print('message recieved')
    channel = client.get_channel(1053858714911776790)
    if message.guild is None and not message.author.bot:
        output='DM from user <@'+str(message.author.id)+'> to DogmaBot'
        embed=discord.Embed(title=message.content)
        embed.set_author(name=message.author.display_name+'#'+message.author.discriminator,icon_url=message.author.avatar)
        await channel.send(output, embed=embed)
        print('forwarded to #moderators-only')


    
# Welcome users

# @client.event
# async def on_member_join(member):
    
# # Say goodbye to users

# @client.event
# async def on_member_remove(member):


#Commands

tree = app_commands.CommandTree(client)

#@tree.command(name = "test", description="test", guild=discord.Object(id=1053851544765874216))
#async def self(Interaction:discord.Interaction):    
#    await Interaction.response.send_message('I say nothing')

#@tree.command(name="buttontest", description="test the button",guild=discord.Object(id=1053851544765874216))
#async def self(Interaction:discord.Interaction):

    #button=Button(label="Click Me!", style=discord.ButtonStyle.green, emoji="<:frank3:1040422477433675857>")

    #async def button_callback(interaction_):
    #   await interaction_.response.send_message("Why did you click me 😭")

    #button.callback=button_callback

    #view=View()
    #view.add_item(button)
    #await Interaction.response.send_message("Button", view=view)

@tree.command(name="hours",description="List the operating hours of DogMahal / Ojata Records",guild=discord.Object(id=1053851544765874216))
async def self(Interaction:discord.Interaction):
    await Interaction.response.send_message('DogMahal / Ojata Records is open Tu-Sa from 11a-9p CST')

@tree.command(name="buttonroles",description="Admin Only Command: Send the button roles in #react-roles",guild=discord.Object(id=1053851544765874216))
async def self(Interaction:discord.Interaction):
    sendButtonRoles()
    await Interaction.response.send_message('Success')

@tree.command(name='senddeal',description="Admin Only Command: Use DogmaBot to send deals to those who signed up",guild=discord.Object(id=1053851544765874216))
async def self(Interaction:discord.Interaction, message:str):
    usercount=0
    for member in Interaction.guild.get_role(1055600368236646471).members:
        user = await member.create_dm()
        await user.send(message)
        usercount=usercount+1
    await Interaction.response.send_message('Sent deal to ' + str(usercount) + ' users')

@tree.command(name='senddm',description="Admin Only Command: Send a DM via DogmaBot",guild=discord.Object(id=1053851544765874216))
async def self(Interaction:discord.Interaction, userid:str, message:str):
    # waiting=True
    # async def waitloop():
    #     dots='.'
    #     while waiting == True:
    #         time.sleep(1)
    #         await Interaction.edit_original_response(content='Sending'+dots+' `'+message+'` to <@'+userid+'>')
    #         dots=dots+'.'
    #         if len(dots) == 15:
    #             await Interaction.edit_original_response(content='Sending `'+message+'` to <@'+userid+'> Failed!')
    #             break

    await Interaction.response.send_message('Sending `'+message+'` to <@'+userid+'>')
    try:
        dm=await client.get_user(int(userid)).create_dm()
        await dm.send(message)
    except AttributeError:
        await Interaction.edit_original_response(content='Sending `'+message+'` to <@'+userid+'> Failed!! (User is a Bot)')
    except ValueError: 
        await Interaction.edit_original_response(content='Sending `'+message+'` to <@'+userid+'> Failed!! (Invalid User)')
    except discord.HTTPException as err:
        if err.code == 50007:
            await Interaction.edit_original_response(content='Sending `'+message+'` to <@'+userid+'> Failed!! (Cannot send messages to this user)')
        else:
            await Interaction.edit_original_response(content='Sending `'+message+'` to <@'+userid+'> Failed!! (Unknown HTTP Error, contact <@348935840501858306> for help)')
    except:
        await Interaction.edit_original_response(content='Sending `'+message+'` to <@'+userid+'> Failed!! (Unknown Error, contact <@348935840501858306> for help)')
    else:
        await Interaction.edit_original_response(content='Sent `'+message+'` to <@'+userid+'>')

@tree.command(name='debug_senddm',description="Admin Only Command: Debug the /senddm command (Don't use unless you know what you're doing)",guild=discord.Object(id=1053851544765874216))
async def self(Interaction:discord.Interaction, userid:str, message:str):
    # waiting=True
    # async def waitloop():
    #     dots='.'
    #     while waiting == True:
    #         time.sleep(1)
    #         await Interaction.edit_original_response(content='Sending'+dots+' `'+message+'` to <@'+userid+'>')
    #         dots=dots+'.'
    #         if len(dots) == 15:
    #             await Interaction.edit_original_response(content='Sending `'+message+'` to <@'+userid+'> Failed!')
    #             break

    await Interaction.response.send_message('Sending `'+message+'` to <@'+userid+'>')
    dm=await client.get_user(int(userid)).create_dm()
    await dm.send(message)
    await Interaction.edit_original_response(content='Sent `'+message+'` to <@'+userid+'>')

    # waiting=False 

    
# Polling

@tree.command(name='poll',description='Make a poll',guild=discord.Object(id=1053851544765874216))
async def embed(Interaction:discord.Interaction, question:str, option1: str, option2: str, option3: str=None, option4: str=None, option5: str=None, option6: str=None, option7: str=None, option8: str=None, option9: str=None, option10: str=None):
    await Interaction.response.send_message('Creating Poll',ephemeral=True)
    description='1️⃣ '+option1+'\n\n2️⃣ '+option2

    if option3 != None:
        description+='\n\n3️⃣ '+option3
    if option4 != None:
        description+='\n\n4️⃣ '+option4
    if option5 != None:
        description+='\n\n5️⃣ '+option5
    if option6 != None:
        description+='\n\n6️⃣ '+option6
    if option7 != None:
        description+='\n\n7️⃣ '+option7
    if option8 != None:
        description+='\n\n8️⃣ '+option8
    if option9 != None:
        description+='\n\n9️⃣ '+option9
    if option10 != None:
        description+='\n\n🔟 '+option10
    
    embed=discord.Embed(title=question, description=description, color=discord.Color.green())
    embed.set_author(name=Interaction.user.name,icon_url=Interaction.user.avatar)
    channel=Interaction.channel_id
    poll= await client.get_channel(channel).send(embed=embed)
    await poll.add_reaction('1️⃣')
    await poll.add_reaction('2️⃣')
    if option3 != None:
        await poll.add_reaction('3️⃣')
    if option4 != None:
        await poll.add_reaction('4️⃣')
    if option5 != None:
        await poll.add_reaction('5️⃣')
    if option6 != None:
        await poll.add_reaction('6️⃣')
    if option7 != None:
        await poll.add_reaction('7️⃣')
    if option8 != None:
        await poll.add_reaction('8️⃣')
    if option9 != None:
        await poll.add_reaction('9️⃣')
    if option10 != None:
        await poll.add_reaction('🔟')


@tree.command(name='whoreacted',description='Get a list of who reacted using what',guild=discord.Object(id=1053851544765874216))
async def self(Interaction:discord.Interaction, messageid:str, poll:bool):
    await Interaction.response.send_message('Gathering...')
    channel=Interaction.channel
    message=await channel.fetch_message(int(messageid))
    users=list()
    for msgreaction in message.reactions:
        #print(msgreaction)
        async for user in msgreaction.users():
            #print(user)
            thing=str(msgreaction)+' '+str(user)
            users.append(str(thing))
    users.sort()
    reeeee=''
    for one in users:
        if poll==True:
            if one.endswith('Bitey Frank#4533') == False:

                reeeee+=one+'\n'
        else:
            reeeee+=one+'\n'
    embed=discord.Embed(title='Who reacted to \"'+str(messageid)+'\"', description=reeeee, color=discord.Color.green())
    embed.set_author(name=Interaction.user.name,icon_url=Interaction.user.avatar)
    await channel.send(embed=embed)


@tree.command(name='polltotal',description='Get a tally of a poll',guild=discord.Object(id=1053851544765874216))
async def self(Interaction:discord.Interaction,messageid:str):
    await Interaction.response.send_message('Calculating...')
    author=Interaction.user.name
    authorIcon=Interaction.user.avatar
    channel=Interaction.channel
    message=await channel.fetch_message(int(messageid))
    users=list()
    for msgreaction in message.reactions:
        #print(msgreaction)
        async for user in msgreaction.users():
            #print(user)
            thing=str(msgreaction)+' '+str(user)
            users.append(str(thing))
    
    users.sort()
    totalPollers=len(users)
    for user in users:
        if user.endswith('Bitey Frank#4533'):
            totalPollers-=1
    onePollers=-1
    twoPollers=-1
    threePollers=-1
    fourPollers=-1
    fivePollers=-1
    sixPollers=-1
    sevenPollers=-1
    eightPollers=-1
    ninePollers=-1
    tenPollers=-1
    #pollEmbed=discord.Embed.copy(message)
    msg="""Poll: '+str(pollEmbed.title)+'\n'+str(pollEmbed.description)+'\n\n"""'Total Pollers: '+str(totalPollers)+'\n\n'

    for user in users:
        if user.startswith('1️⃣') == True:
            onePollers+=1
        else:
            if user.startswith('2️⃣') == True:
                twoPollers+=1
            else:
                if user.startswith('3️⃣') == True:
                    threePollers+=1
                else:
                    if user.startswith('4️⃣') == True:
                        fourPollers+=1
                    else:
                        if user.startswith('5️⃣') == True:
                            fivePollers+=1
                        else:
                            if user.startswith('6️⃣') == True:
                                sixPollers+=1
                            else:
                                if user.startswith('7️⃣') == True:
                                    sevenPollers+=1
                                else:
                                    if user.startswith('8️⃣') == True:
                                        eightPollers+=1
                                    else:
                                        if user.startswith('9️⃣') == True:
                                            ninePollers+=1
                                        else:
                                            if user.startswith('🔟') == True:
                                                tenPollers+=1


    


    onePollersPercentage=float(onePollers/totalPollers)
    msg+='1️⃣ *'+str(round(onePollersPercentage*100,2))+'%* **('+str(onePollers)+')\n\n**'
    twoPollersPercentage=float(twoPollers/totalPollers)
    msg+='2️⃣ *'+str(round(twoPollersPercentage*100,2))+'%* **('+str(twoPollers)+')\n\n**'
    if users.count('3️⃣') >= 0:
        threePollersPercentage=float(threePollers/totalPollers)
        msg+='3️⃣ *'+str(round(threePollersPercentage*100,2))+'%* **('+str(threePollers)+')\n\n**'
    if users.count('4️⃣') >= 0:
        fourPollersPercentage=float(fourPollers/totalPollers)
        msg+='4️⃣ *'+str(round(fourPollersPercentage*100,2))+'%* **('+str(fourPollers)+')\n\n**'
    if users.count('5️⃣') >= 0:
        fivePollersPercentage=float(fivePollers/totalPollers)
        msg+='5️⃣ *'+str(round(fivePollersPercentage*100,2))+'%* **('+str(fivePollers)+')\n\n**'
    if users.count('6️⃣') >= 0:
        sixPollersPercentage=float(sixPollers/totalPollers)
        msg+='6️⃣ *'+str(round(sixPollersPercentage*100,2))+'%* **('+str(sixPollers)+')\n\n**'
    if users.count('7️⃣') >= 0:
        sevenPollersPercentage=float(sevenPollers/totalPollers)
        msg+='7️⃣ *'+str(round(sevenPollersPercentage*100,2))+'%* **('+str(sevenPollers)+')\n\n**'
    if users.count('8️⃣') >= 0:
        eightPollersPercentage=float(eightPollers/totalPollers)
        msg+='8️⃣ *'+str(round(eightPollersPercentage*100,2))+'%* **('+str(eightPollers)+')\n\n**'
    if users.count('9️⃣') >= 0:
        ninePollersPercentage=float(ninePollers/totalPollers)
        msg+='9️⃣ *'+str(round(ninePollersPercentage*100,2))+'%* **('+str(ninePollers)+')\n\n**'
    if users.count('🔟') >= 0:
        tenPollersPercentage=float(tenPollers/totalPollers)
        msg+='🔟 *'+str(round(tenPollersPercentage*100,2))+'%* **('+str(tenPollers)+')\n\n**'
    embed=discord.Embed(title='Tallied Votes',description=msg,color=discord.Color.green())
    embed.set_author(name=author,icon_url=authorIcon)
    await channel.send(embed=embed)




    # else:
    #     await Interaction.response.send_message('You lack permissions')

#@tree.command()


#React Roles


#@tree.command(name="activatereactroles", description="Send the react role messages",guild=discord.Object(id=1053851544765874216))
#@has_permissions(manage_roles=True)
#async def self(Interaction:discord.Interaction):
#    await Interaction.response.send_message('success')
client.run(TOKEN)