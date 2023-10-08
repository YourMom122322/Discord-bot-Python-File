import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author.bot:
        return  # Ignore messages from bots

    if message.content.lower() == '1zombie_chaos':
        await message.channel.send('This server got attacked by Zombies')
        while True:
            response = await bot.wait_for('message', check=lambda m: m.author == message.author)
            if response.content.lower() == '!stop chaos':
                break
            else:
                await message.channel.send('zombie')

    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    await ctx.send('@everyone Pong!')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command()
async def roll(ctx):
    import random
    await ctx.send(f'You rolled a {random.randint(1, 6)}')

@bot.command()
async def clear(ctx):
    def is_not_server_owner(m):
        return m.author != ctx.guild.owner
    
    await ctx.channel.purge(check=is_not_server_owner)
    await ctx.send("Messages cleared.", delete_after=5)

@bot.command()
async def commands(ctx):
    command_list = [
        'ping: Responds with "@everyone Pong!"',
        'hello: Responds with "Hello!"',
        'roll: Generates a random number between 1 and 6 and sends the result',
        'clear: Clears messages in the channel, but doesn\'t delete messages from the server owner',
        'commands: Lists all available commands excluding secret_commands, create_myself_or_die_at_3_am, delete_myself_or_die_at_3_am, DONT_KILL_ME, KILL_ME'
    ]

    command_text = '\n'.join(command_list)
    await ctx.send(f'Available commands:\n```{command_text}```')

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run('YOUR_BOT_TOKEN')
