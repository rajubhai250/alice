import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID =25251663
API_HASH = "8e7e485d18470e56d6d918a8d928da61"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7923114293:AAH1ZsI_tXAA6QMT-zzFi50ZjZhP9Nh2KG8"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://Cluster0:Cluster0@cluster0.fybot.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID =-4525975521

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID =7140355547

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/thanos_pro"
SUPPORT_GROUP = "https://t.me/ott_store_discussion_group"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQAf70YAdKAmyRsIPH2exoA4LHynHZ-du8jz466MRmvLW7CnmprjeSgefm5YVC7WkFP_sGbobojCnutBwN14q_UwmCMcraHxdmQvM-Ecg86TEUvL7bg6WtQa48KXJ3QmBjWba4AWTYyMST1EYU_Un2Koq_SDxsHeBxZZRDiMWlItuGs0sXurfGBQh4kGWN-1hkRSBxs49Baq1ZCQBvBTZlz_Ap60ZpjD_weUBLiHrlOeX2NQIPXA32pICQSrdQnjOZfBrTmJPcC-2cdJW1oaMfqs0eWRB8n6Bqa8eEiC16QKVK8B6T1pDLog1YVKwH_Ctnc_tYGpT0OAr2oxYYC02eaiLci56gAAAAGpmS3bAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://graph.org/file/46f33117899dd638d9b1a-a4233e90a10d0d7f55.jpg"

PING_IMG_URL = "https://graph.org/file/46f33117899dd638d9b1a-a4233e90a10d0d7f55.jpg"

PLAYLIST_IMG_URL = "https://graph.org/file/763a841a2ad5cbb1e2fc5.jpg"
STATS_IMG_URL = "https://graph.org/file/f586172fe40a0b5d0b0df.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
TELEGRAM_VIDEO_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
