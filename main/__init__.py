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
SESSION = BQFZJBwAbt_ZHLcqaxUt8P20AllBaehHwMIdsOAq5N1XBTouqvabufE-DcBPuk2KoggAryUT3xz7gKWurs2K4LyBXk5SgRGjqYTa6hgk635t9dIQJ651W5BgrvmQiFeU-FS9PVEeAtXb4_0jgkJr1UYUV9v5LgutLdmJNnkrhSiADp2p4Ihv-USZP-pyQxxRz4xtWInT3hEXVBDIrQRbdYz63BEvnkEroi7V7RF1FwsT8odWbTYa4-T_3I5SWB3xSZkIjYNcnoEu6T2yDFSK9qnWGrfnkro2mofytgRsTg7wwq4GW4LLPtozgUIGkVbh0msLOseL61HDhTzKh8ugHik-zEFKzQAAAAGYNL3-AA
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
