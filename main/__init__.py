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
SESSION = "BQFZJBwAptYCyda0taJ-I--wlxd9Cg-KbPt0bSgiVoLj4h3VcGflkGNRiipbNZd8lvQOSjUZWQVR1YgDiPGlVTqTNDWZUyxQxznyQwSlnWEG6PsW7YV6TkIgDZxPu67kXnDS7Uh5PbtJRpMXAQ24QgqwAiugabBprvlvcpTvRCAhiujCv6bKEZglTLyALEVziVTej1QA7xOxpD0ieXnGJNmXMdew106riOMcSEwU0d-BpyxPTtxsGPeQMBs_zghjakWrC_-t3jh7I49DNvgfRNpopplNatK28vu13Gsr3t_fLH4jaUHwbhxai1SUqI1UxC6iLWt5ulY763UA93RzsjuOfShWwAAAAAGYNL3-AA"
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
