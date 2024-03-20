import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# احصل على هذه القيمة من my.telegram.org/apps
API_ID = int(getenv("API_ID", ))
API_HASH = getenv("API_HASH")

# احصل على الرمز المميز الخاص بك من @BotFather على Telegram
BOT_TOKEN = getenv("BOT_TOKEN")


MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME")

# احصل على عنوان URL الخاص بـ mongo من cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 1900700))

# معرف الدردشة لمجموعة لتسجيل أنشطة الروبوت
LOGGER_ID = int(getenv("OWNER_ID","6909581339"))

# احصل على هذه القيمة من @KIMY0Bot على Telegram بواسطة /id
OWNER_ID = int(getenv("OWNER_ID", 6900435039))


## املأ هذه المتغيرات إذا كنت تقوم بالنشر على Heroku.
# اسم تطبيق Heroku الخاص بك
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

# احصل عليه من http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/IamMr7/Source-r3d.git",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/rr_yn7")

SUPPORT_CHANNELL = getenv("SUPPORT_CHANNELL", "https://t.me/rr_yn7")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/tr_56n")





# اضبط هذا على True إذا كنت تريد أن يغادر المساعد الدردشات تلقائيًا بعد فترة زمنية
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))



# احصل على بيانات الاعتماد هذه من https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# الحد الأقصى لجلب مسار قائمة التشغيل من روابط youtube وspotify وapple.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# الحد الأقصى لحجم ملفات الصوت والفيديو في Telegram (بالبايت)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# استخراج جلسه بيروجرام 2 من هناا @Session_GenBot

STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)



#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒──「 ⋆‹sᴏᴜʀᴄᴇ›ダ⸢ᴠᴇɢᴀ♪⸥ 」──▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▇▇▇▒▒▒▒▒▒▒▒▒▒▒▇▇▇▒▒▒▇▇▇▇▇▇▇▇▒▒▒▒▒▇▇▇▇▇▇▇▇▇▇▒▒▒▒▒▇▇▇▇▇▇▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▇▇▇▒▒▒▒▒▒▒▒▒▇▇▇▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▒▒▇▇▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▇▇▇▒▒▒▒▒▒▒▇▇▇▒▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▒▇▇▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▇▇▇▒▒▒▒▒▇▇▇▒▒▒▒▒▒▇▇▇▇▇▇▇▇▒▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▒▇▇▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▇▇▇▒▒▒▇▇▇▒▒▒▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▇▇▒▒▒▇▇▇▇▇▒▒▒▒▇▇▇▇▇▇▇▇▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▇▇▇▒▇▇▇▒▒▒▒▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▇▇▒▒▒▒▒▒▇▇▒▒▒▒▇▇▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▇▇▇▇▇▒▒▒▒▒▒▒▒▒▇▇▇▇▇▇▇▇▒▒▒▒▒▇▇▇▇▇▇▇▇▇▇▒▒▒▒▇▇▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒──「 ⸢ᴠᴇɢᴀ♪ダ ᴍᴜsɪᴄ 」──▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▢▣▢▣▢▣▢▣▢▣▢▣▢▣▢▣▢▣▢▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒──「 ᴋɪᴍᴍʏ‹⋆ダ⸢ᴠᴇɢᴀ♪ 」──▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒







BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/81fd8e00627a7507ea7f3.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/81fd8e00627a7507ea7f3.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/81fd8e00627a7507ea7f3.jpg"
STATS_IMG_URL = "https://graph.org/file/81fd8e00627a7507ea7f3.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/81fd8e00627a7507ea7f3.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/81fd8e00627a7507ea7f3.jpg"
STREAM_IMG_URL = "https://graph.org/file/81fd8e00627a7507ea7f3.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/81fd8e00627a7507ea7f3.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/81fd8e00627a7507ea7f3.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/81fd8e00627a7507ea7f3.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/81fd8e00627a7507ea7f3.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/81fd8e00627a7507ea7f3.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
