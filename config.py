import os
import logging
from logging.handlers import RotatingFileHandler

# Helper function to safely get integer environment variables
def get_int_env_var(name: str, default: int = 0) -> int:
    try:
        value = os.environ.get(name, "").strip()
        return int(value) if value else default
    except ValueError:
        return default

# Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

# Your API ID from my.telegram.org
APP_ID = get_int_env_var("APP_ID")

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

# Your db channel Id
CHANNEL_ID = get_int_env_var("CHANNEL_ID")

# NAMA OWNER
OWNER = os.environ.get("OWNER", "sukumarnanda")

# OWNER ID
OWNER_ID = get_int_env_var("OWNER_ID")

# Port
PORT = os.environ.get("PORT", "8030")

# Database
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "")

# Force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = get_int_env_var("FORCE_SUB_CHANNEL")
FORCE_SUB_CHANNEL2 = get_int_env_var("FORCE_SUB_CHANNEL2")

TG_BOT_WORKERS = get_int_env_var("TG_BOT_WORKERS", 4)

FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "")) # auto delete in seconds

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/8784a1e815fcd20eff3a4.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://telegra.ph/file/8784a1e815fcd20eff3a4.jpg")

HELP_TXT = (
    "<b>📁 File Link BOT for ModderSU.COM</b>\n\n"
    "<b>❏ BOT COMMANDS</b>\n"
    "├ <code>/start</code> : Start the bot\n"
    "├ <code>/about</code> : Bot information\n"
    "└ <code>/help</code> : Help menu\n\n"
    "🔗 Just click on a link, start the bot, join both channels, and try again. That's it!\n\n"
    "👨‍💻 Developed by <a href='https://t.me/sukumarnanda'>Sukumar</a>"
)

ABOUT_TXT = (
    "<b>◈ Creator:</b> <a href='https://t.me/sukumarnanda'>Sukumar</a>\n"
    "<b>◈ Founder of:</b> <a href='https://liteapks.org'>LITEAPKS</a>\n"
    "<b>◈ Partner Site:</b> <a href='https://moddersu.com'>ModderSU</a>"
)


START_MSG = os.environ.get("START_MESSAGE", 
    "<b>This bot is not available in your region.</b>"
)


try:
    ADMINS = [6376328008]
    for x in (os.environ.get("ADMINS", "").split()):
        if x.strip():  # Check if the string is not empty
            ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

# Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}\n\n<b>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b>")

# Set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ https://moddersu.com.</b>")

# Set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

# Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "This Bot is not available in your region."

ADMINS.append(OWNER_ID)
ADMINS.append(5191566338)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
