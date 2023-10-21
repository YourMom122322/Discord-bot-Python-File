import discord
from discord.ext import commands
import random
from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def keep_alive():
    return "Keep alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def start():
    server_thread = threading.Thread(target=run)
    server_thread.start()

if __name__ == '__main__':
    start()

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Bot is ready')

@bot.command()
async def ping(ctx):
    await ctx.send('Ping!')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command()
async def roll(ctx):
    await ctx.send(random.randint(1, 6))

bot.run('YOUR_BOT_TOKEN')
