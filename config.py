import re
import os
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

# Load .env file
load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

# Limit durasi lagu (default 9999 menit)
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 9999))

# Chat ID untuk logging aktivitas bot
LOGGER_ID = int(getenv("LOGGER_ID", None))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 5734902794))

## Heroku configuration
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# ==============================
# 📦 COOKIES YOUTUBE
# ==============================
# Bisa diatur lewat env MYCOOKIES, atau fallback ke cookies.txt
_mycookies_env = getenv("MYCOOKIES", "cookies.txt")
mycookies = os.path.abspath(os.path.expanduser(_mycookies_env))

# Jika file cookies tidak ditemukan, tampilkan warning
if not os.path.exists(mycookies):
    print(f"[WARNING] File cookies tidak ditemukan di: {mycookies}")
    print("Pastikan path benar atau atur variabel MYCOOKIES di .env")

# ==============================

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/elzahraku/YoutubeMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)  # untuk private repo

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/eLzStore_id")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/YtMusicClub")

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# Spotify API credentials
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

# Playlist fetch limit
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 1000))

# Telegram file size limits
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))

# Pyrogram session strings
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

# Filters dan variabel runtime
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# Image URLs
DEFAULT_IMG = "https://graph.org/file/ef42f9cf292601c7f0458-90aee4fbc91d7db61c.jpg"
START_IMG_URL = getenv("START_IMG_URL", DEFAULT_IMG)
PING_IMG_URL = getenv("PING_IMG_URL", DEFAULT_IMG)
PLAYLIST_IMG_URL = getenv("PLAYLIST_IMG_URL", DEFAULT_IMG)
STATS_IMG_URL = getenv("STATS_IMG_URL", DEFAULT_IMG)
TELEGRAM_AUDIO_URL = getenv("TELEGRAM_AUDIO_URL", DEFAULT_IMG)
TELEGRAM_VIDEO_URL = getenv("TELEGRAM_VIDEO_URL", DEFAULT_IMG)
STREAM_IMG_URL = getenv("STREAM_IMG_URL", DEFAULT_IMG)
SOUNCLOUD_IMG_URL = getenv("SOUNCLOUD_IMG_URL", DEFAULT_IMG)
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", DEFAULT_IMG)
SPOTIFY_ARTIST_IMG_URL = getenv("SPOTIFY_ARTIST_IMG_URL", DEFAULT_IMG)
SPOTIFY_ALBUM_IMG_URL = getenv("SPOTIFY_ALBUM_IMG_URL", DEFAULT_IMG)
SPOTIFY_PLAYLIST_IMG_URL = getenv("SPOTIFY_PLAYLIST_IMG_URL", DEFAULT_IMG)

# Waktu ke detik
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

# Total durasi limit
DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# Validasi URL
if SUPPORT_CHANNEL and not re.match("(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit(
        "[ERROR] - SUPPORT_CHANNEL url salah. Harus diawali dengan https://"
    )

if SUPPORT_CHAT and not re.match("(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit(
        "[ERROR] - SUPPORT_CHAT url salah. Harus diawali dengan https://"
    )

print(f"[INFO] Loaded mycookies path: {mycookies}")
