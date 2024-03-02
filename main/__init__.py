#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 22619164
API_HASH = "0c1dba6801e2fb8c47ca89d150e2879f"
BOT_TOKEN = "6738441525:AAES7BC8c7gtg4jcY1psSbvJjccoG-3gfyY"
SESSION = BQAivtHlAOKMJe17TRJ8vN_a6g47JyRDXTCoEKJC0Og5aiFxRdZA8Kl1IHwlk7ReuwyvfoWNBUT7x4-Dr47wiGWsYZRtzus_0oucsfX7gXxlhR1pj7FyeKqq6ADivLT24-rSF7jQpU-iZ7kDSKdDs2r0zLPHFXwOwdLVdAM1HtPnOl0naZuQcob3uAeoDBrJmCLVAWa3SnU9YNVRIySIQdFVVuGGlqhlbydLNQhL0We5Ooah8DSVtbSZWauBoNQeA2iyQB8bTTiRg7zbUY64ORT8SSBy5SybPJIMiHqzfrL69qgHZuFZpLgV63gcD48cOqDelgmVeG2gdJhIVH0vNy_JAAAAAZg0vf4A
FORCESUB = "savescrb"
AUTH = 6848560638

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
