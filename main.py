import traceback
import discord
from discord.ext import commands
import os
import dotenv

# cwdをこのファイルがある場所に移動
os.chdir(os.path.dirname(os.path.abspath(__file__)))


dotenv.load_dotenv()

bot = commands.Bot(intents=discord.Intents.all(), command_prefix="tca!")

@bot.event
async def on_ready():
    await bot.load_extension("jishaku")
    for name in os.listdir("./cogs"):
        if not name.startswith((".", "_")):
            try:
                await bot.load_extension("cogs."+name.replace(".py", ""))
            except Exception as e:
                print("".join(traceback.format_exception(e)))
    await bot.tree.sync()
    print("Hello, TCABot!")


bot.run(token=os.getenv("TCABOT_TOKEN"))
