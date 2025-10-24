import discord
from discord.ext import commands
import asyncio
import logging
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv() 

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(name)s: %(message)s')

# Bot intents
intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.reactions = True
intents.message_content = True

# Bot initialization
bot = commands.Bot(command_prefix='/', intents=intents)

# Slash command to vote for banning a member
@bot.slash_command(guild_ids=[os.getenv("GUILD_ID")], description="Vote to ban a member")
async def voteban(ctx, member: discord.Member, reason: str):
    # Check if the author has the 'Legacy Members' role
    member_role_id = os.getenv("MEMBER_ROLE_ID")  # Make sure this is the correct role ID
    if member_role_id not in [role.id for role in ctx.author.roles]:
        await ctx.respond("You do not have the required role to use this command.")
        return

    # Prevent banning users with a role equal to or higher than the author's
    if member.top_role >= ctx.author.top_role or member == ctx.guild.owner:
        await ctx.respond("You cannot vote to ban someone with an equal or higher role.")
        return

    # Send initial message and wait for reactions
    message = await ctx.respond(f"Vote to ban {member.display_name} for: {reason}. Countdown of **5 minutes** started until votes end! React with 👍 to ban or 👎 not to ban.")
    message = await message.original_response()
    await message.add_reaction("👍")
    await message.add_reaction("👎")

    # Wait for 5 minutes
    await asyncio.sleep(300)

    # Refresh the message to get updated reactions
    message = await ctx.channel.fetch_message(message.id)
    count_up = 0
    count_down = 0

    for reaction in message.reactions:
        if str(reaction.emoji) == "👍":
            count_up = reaction.count - 1  # Exclude the bot's vote
        elif str(reaction.emoji) == "👎":
            count_down = reaction.count - 1  # Exclude the bot's vote

    # Decision on the ban
    if count_up > count_down:
        await member.ban(reason=reason)
        await ctx.send_followup(f"{member.display_name} has been banned by majority vote. Voting results: {count_up} for, {count_down} against.")
    else:
        await ctx.send_followup(f"{member.display_name} will not be banned. Voting results: {count_up} for, {count_down} against.")

# Start the bot
bot.run(os.getenv("DISCORD_TOKEN"))
