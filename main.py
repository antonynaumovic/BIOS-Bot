import discord
import random
import traceback
import os
from discord.ext import commands

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()



def get_prefix(client, message):

    prefixes = ['=', '==']    # sets the prefixes, u can keep it as an array of only 1 item if you need only one prefix

    if not message.guild:
        prefixes = ['==']   # Only allow '==' as a prefix when in DMs, this is optional

    # Allow users to @mention the bot instead of using a prefix when using a command. Also optional
    # Do `return prefixes` if u don't want to allow mentions instead of prefix.
    return commands.when_mentioned_or(*prefixes)(client, message)


client = commands.Bot(                         # Create a new bot
    command_prefix=get_prefix,              # Set the prefix
    description='A BIOS Bot',  # Set a description for the bot
    owner_id=258295063635951618,            # Your unique User ID
    case_insensitive=True                   # Make the commands case insensitive
)




@client.event
async def on_ready():
    print("Started")
    for s in client.guilds:
        for channel in s.channels:
            if channel.name == "rules-and-regulations" or channel.id == "419931020771459072":
                global rules
                rules = channel


@client.command(pass_context=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)

@client.event
async def on_member_update(before, after):
    pass
    n = after.nick
    if after.nick != "Mke" and after.id != 145926021051449355:
        try:
            await after.edit(nick="Mke")
        except Exception:
            pass
    

@client.event
async def on_raw_reaction_add(payload):
    if payload.user_id != "584807152669950132":

        server = client.get_guild(payload.guild_id)

        channel = payload.channel_id

        member = server.get_member(payload.user_id)
        print(member)

        emoji = client.get_emoji(payload.emoji.id)

        print(payload.emoji.name)

        limited = discord.utils.get(member.guild.roles, name="Limited")
        community = discord.utils.get(member.guild.roles, name="Community")
        dj = discord.utils.get(member.guild.roles, name="DJ")

        if payload.emoji.name == '✅':
            print("yeet")
            try:
                await member.remove_roles(limited)
                await member.add_roles(community)
                await member.add_roles(dj)
            except Exception:
                print("Couldn't Remove role for {}".format(member))
                traceback.print_exc()
                pass


@client.event
async def on_member_join(member):
    limited = discord.utils.get(member.guild.roles, name="Limited")
    await member.add_roles(limited)


@client.event
async def on_message(message):
    id = client.get_guild(419928725304508417)
    channels = ["commands", "bot-test", "bot-spam🔊", "rules-and-regulations"]
    print('Message from {0.author}: {0.content}'.format(message))

    if str(message.channel) in channels:

        if message.content.find("!esl") != -1:
            embed = discord.Embed(title="ESL Custom Match ", color=0xd9003d)
            embed.set_author(name="ESL Settings",
                             url="https://play.eslgaming.com/rainbowsix/europe-pc/r6siege/open/ladder-5on5-europe/",
                             icon_url="https://cdn0.iconfinder.com/data/icons/Modern_Web_Social_Icons_by_SimekOneLove/256/esl.png")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/534060236429066251/584818099438485528/Bios_Circle.png")
            embed.add_field(name="Information:", value="Lion, Gridlock and Mozzie are not allowed to be used!",
                            inline=False)
            embed.add_field(name="Tournament:", value="Matches Bo2", inline=False)
            embed.add_field(name="Requirements: (PC only)", value="ESL Anticheat", inline=True)
            embed.add_field(name="Match Settings:",
                            value="Number of Bans: 4 \n Ban Timer: 20 \n Number of Rounds: 12 \n Attacker/Defender Role swap: 6 \n Overtime: 3 \n Overtime Score Difference: 2 \n Overtime Role Change: 1 \n Objective Rotation Parameter: 2 \n Objective Type Rotation: Rounds Played Attacker \n Unique Spawn: On Pick Phase Timer: 15 \n 6TH Pick Phase: On \n 6TH Pick Phase Timer: 15 \n Reveal Phase Timer: 5 \n Damage Handicap: 100 \n Friendly Fire Damage: 100 \n Injured: 20 \n Sprint: On \n Lean: On \n Death Replay: Off",
                            inline=False)
            embed.add_field(name="Standard ESL Map Pool:",
                            value="Bank \n Border \n Club House \n Coastline \n Consulate \n Villa \n Oregon",
                            inline=True)
            await message.channel.send(embed=embed)

        elif message.content.find("bueh bueh")!= -1:
            await message.channel.send("A wimbueh")
            await message.channel.send("A wimbueh")
            await message.channel.send("eeeeehhhhh eeeeehhhh")
            await message.channel.send("A weeee umbumbueh")
            await message.channel.send("In the Jungle, the mighty jungle, the lion sleeps tonight")
            await message.channel.send("A wimbueh")
            
        elif message.content.find("natus")!= -1:
            await message.channel.send("Natssu's a bad cunt")
            
        elif message.content.find("lmao yeet")!= -1:
            if message.author.id == 258295063635951618:
                role = discord.utils.get(message.author.guild.roles, name="Admin")
                role2 = discord.utils.get(message.author.guild.roles, name="Maximum Co-OwnerSayian")
                await message.author.add_roles(role)
                try:
                    await message.author.add_roles(role2)
                except Exception:
                    pass
                
            elif message.author.id == 612388606425694247:
                role = discord.utils.get(message.author.guild.roles, name="Limited")
                await message.author.add_roles(role)
            
        elif message.content.find("!nuke")!= -1:
            await message.channel.send("3")
            await message.channel.send("2")
            await message.channel.send("1")
            await message.channel.send("0")
            await message.channel.send("Lmao Pranked")
            
        elif message.content.find("i am mke") != -1:
            roleList = []
            role = discord.utils.get(message.author.guild.roles, name="Admin")
            for i in message.author.roles:
                roleList.append(i)
            if role in roleList:
                for user in message.guild.members:
                    try:
                        await user.edit(nick="Mke")
                        print("changed {}'s name to mke".format(user))
                    except Exception:
                        pass
                await message.channel.send("I Am Mke")
                    
                
            
        elif message.content.find("!users") != -1:
            await message.channel.send(f"""Number Of Members = {id.member_count}""")

        elif message.content.find("!map") != -1:

            maps = ["Bank", "Border", "Club House", "Consulate", "Coastline", "Oregon", "Villa"]

            embed = discord.Embed(title="Random ESL Map", color=0xd9003d)
            embed.set_author(name="",
                             url="https://play.eslgaming.com/rainbowsix/europe-pc/r6siege/open/ladder-5on5-europe/",
                             icon_url="https://cdn0.iconfinder.com/data/icons/Modern_Web_Social_Icons_by_SimekOneLove/256/esl.png")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/534060236429066251/584818099438485528/Bios_Circle.png")

            embed.add_field(name="Map:", value=random.choice(maps), inline=False)

            await message.channel.send(embed=embed)


        elif message.content.find("!no") != -1:
            await message.channel.send("no")

        elif message.content.find("!banner") != -1:
            file = discord.File("img/Banner.png", filename="img/Banner.png")
            await message.channel.send(file=file)

        elif message.content.find("!rules") != -1:
            embed = discord.Embed(title="Server Rules:", color=0xd9003d)
            embed.set_author(name="RULES: ACCEPT RULES BY CLICKING GREEN TICK")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/534060236429066251/584818099438485528/Bios_Circle.png")
            embed.add_field(name="1.",
                            value="-Any serious toxicity will be treated with a warning system, 3 warnings will result in a kick then a ban 2nd time round",
                            inline=False)
            embed.add_field(name="2.",
                            value="-Any sexual content or nsfw content will have 1 post ONLY after that it is a kick then a permanent Ban",
                            inline=False)
            embed.add_field(name="3.",
                            value="-Any bullshittery or so on will be treated with a kick then a Permanent Ban",
                            inline=False)
            embed.add_field(name="4.",
                            value="-Any of these that are posted outside of the shitchat will be treated with an immedite kick then ban if followed on after",
                            inline=False)
            embed.add_field(name="5.", value="-No Racism", inline=False)
            embed.add_field(name="6.", value="-Respect Admins", inline=False)
            embed.add_field(name="7.", value="-Respect All Members", inline=False)
            embed.add_field(name="8.",
                            value="-If you want to advertise your Discord in here that's fine, just dm Natsu about it first",
                            inline=False)
            embed.add_field(name="9.",
                            value="-if you are also found screwing with the bots it will be an automatic ban",
                            inline=False)
            embed.add_field(name="10.", value="-ACCEPT RULES TO GAIN A ROLE BY CLICKING GREEN TICK", inline=False)
            embed.set_footer(text="Thank You.")
            #rulesPost = await rules.send(embed=embed)
            #await rulesPost.add_reaction("✅")

            await client.process_commands(message)

client.run(os.getenv('TOKEN'), bot=True, reconnect=True)
