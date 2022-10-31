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

STRING_SESSION = getenv("STRING_SESSION","BQCH208TkPysSyQGC85uN0nqK_jPUHa0DOtZuNYJlqastWOnkq_zyyGHr_vZMbpITHdxI4v_qleN8Ug-S8ZGqgRXryiWVdG2xhkfvDVegs2gozwEuvnZeC3vgYKxMDQu2eKmOffRgHb070LpHtdIRS_bUe0fEUPVt8eWTtfRj3oYhH39K_GnmErLCr3iy6Ai933lvvVPVz1aAN90dBS0kdpdz10DdPdESwSQChDkDvo_05RM_-1NR_09Qgz3e38vyj5S412jysVpmDBYWoM_RIJYOBmRN_Q50AhnqULu7iDmDT30XJx91vWWZoyLRBSB-jI5gX6brxF5kjX55mdwZd4Le7fKQAA")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2046092634").split()))
