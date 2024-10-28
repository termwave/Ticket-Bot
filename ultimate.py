import os
import discord
from discord.ext import commands
import datetime
import asyncio
from discord.ext.commands.errors import ExtensionAlreadyLoaded, ExtensionNotFound
from datetime import datetime
import psutil
os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True"
os.environ["JISHAKU_HIDE"] = "True"
os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
os.environ["JISHAKU_FORCE_PAGINATOR"] = "True"
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents, owner_ids=[1188712861510422549,920649604092014623])
bot.remove_command("help")

token = ""
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    synced_commands = await bot.tree.sync()
    print(f'Synced {len(synced_commands)} slash commands')
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="Tickets"))
    print("Changed presence")
    
async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"Loaded extension: cogs.{filename[:-3]}")
            except ExtensionAlreadyLoaded:
                print(f"Extension already loaded: cogs.{filename[:-3]}")
            except ExtensionNotFound:
                print(f"Extension not found: cogs.{filename[:-3]}")
            except Exception as e:
                print(f"Failed to load extension cogs.{filename[:-3]}: {type(e).__name__} - {e}")
    try:
        await bot.load_extension("jishaku")
        print("Loaded extension: jishaku")
    except ExtensionAlreadyLoaded:
        print("Extension already loaded: jishaku")
    except ExtensionNotFound:
        print("Extension not found: jishaku")
    except Exception as e:
        print(f"Failed to load jishaku: {type(e).__name__} - {e}")


async def main():
    async with bot:
        await load()
        await bot.start(token)

asyncio.run(main())