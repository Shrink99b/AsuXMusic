from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", "13791948"))
API_HASH = getenv("API_HASH","b4534a8924232e4c6bd171da36251094")

ASS_HANDLER = list(getenv("ASS_HANDLER", ".").split())
BOT_TOKEN = getenv("BOT_TOKEN","5544474027:AAG4gH91He35vMs4LMZfu_aqAhXneGzeALA ")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "150"))
LOGGER_ID = int(getenv("LOGGER_ID"," -1001521543298"))
MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://ziddiboy1763:ziddiboy1763@cluster0.ilw31mx.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5099353600").split()))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/c5952790fa8235f499749.jpg")
START_IMG = getenv("START_IMG")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", " https://t.me/hjhvvl ")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", " https://t.me/hjhvvl ")

STRING_SESSION = getenv("STRING_SESSION", None)
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1452219013").split()))
