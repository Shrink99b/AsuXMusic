from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", "13791948"))
API_HASH = getenv("API_HASH","b4534a8924232e4c6bd171da36251094")

ASS_HANDLER = list(getenv("ASS_HANDLER", ".").split())
BOT_TOKEN = getenv("BOT_TOKEN","5544474027:AAG4gH91He35vMs4LMZfu_aqAhXneGzeALA")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "1500"))
LOGGER_ID = int(getenv("LOGGER_ID"," -1001769516312"))
MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://ziddiboy1763:ziddiboy1763@cluster0.ilw31mx.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5099353600").split()))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/2ea8e06e1ead51ef86c7e.jpg")
START_IMG = getenv("START_IMG","https://telegra.ph/file/2ea8e06e1ead51ef86c7e.jpg")

SUPPORT_CHAT = getenv("SUPPORT_CHAT","hjhvvl")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL","hjhvvl")

STRING_SESSION = getenv("STRING_SESSION","AQCqRtGhCtzd_Y-iBuJ4vijwRRFPs527pbCNHsLwqjizyfOBYLYeTDky-E3fGjR-PftUI4NOmb3Py0kLoydCjifmunEemsmO6MO2dfux_iwEyG4XZLPSu9y4KGkmPbSYr80TFEn2zQeTEz0Cj_AJbd5HMuce46UkCcVfjO7EASYyYcFTfa9DXU-HEM5QMgYOEvUAP2TyiYg9_DpNo7T9g51Eix6c9b2P4c7uYLLfoAffaKfwfF3SgVc110TIV1-kpr8PtHBJJm-CmhxuUOKOEE3H--XWWmkE2Oob8X2JpeOo7ECoOaK4lMS9zj8KjrMzoFy-tUHQeqOhvbrNBovLos1wAAAAAUxEzaMA")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2046092634").split()))
