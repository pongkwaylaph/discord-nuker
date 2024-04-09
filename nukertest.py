import discord
from discord.ext import commands


intents = discord.Intents.all()
intents.members = True
intents.typing = True
intents.presences = True

bot = commands.Bot(command_prefix='.', intents=intents)


@bot.event
async def on_ready():
    print('Bot is ready.')


@bot.command()
async def check_status(ctx):
    if not bot.is_ready():
        await ctx.send("The bot is currently logging in...")
    else:
        await ctx.send("The bot is online and ready.")


@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")

@bot.event
async def on_command_error(ctx, error):
    if ctx.command:
        print(f"Error occurred while executing command '{ctx.command.name}': {error}")
    else:
        print(f"Error occurred: {error}")

@bot.command()
async def raid(ctx, amount: int, channel_name: str):
    if ctx.author.guild_permissions.administrator:
        for channel in ctx.guild.channels:
            await channel.delete()

        # Create new channels
        for i in range(amount):
            await ctx.guild.create_text_channel(channel_name)

        await ctx.send(f"Raid completed. {amount} channels created with name '{channel_name}'.")
    else:
        await ctx.send("You don't have permission to use this command.")



@bot.command()
async def stop(ctx):
    for task in asyncio.all_tasks():
        task.cancel()
    await bot.logout()


@bot.command()
async def chnnl(ctx, num: int, name: str):
    if ctx.author.guild_permissions.manage_channels:
        for i in range(num):
            await ctx.guild.create_text_channel(name)
        await ctx.send(f"{num} channels created.")
    else:
        await ctx.send("You don't have permission to use this command.")

@bot.command()
async def spam(ctx, amount: int, *, message: str):
    if ctx.author.guild_permissions.send_messages:
        for i in range(amount):
            await ctx.send(message)
        await ctx.send(f"Sent {amount} messages.")
    else:
        await ctx.send("You don't have permission to use this command.")

# Run the bot
bot.run('YOUR-BOT-TOKEN')
