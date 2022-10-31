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

STRING_SESSION = getenv("STRING_SESSION","BQBYjkzpIH7Ie_RuXLOSNPUDvk2fVYiZqOGKdSiv3U_wW_EaTJN7PENvefHWwUXB7saRbI6rXsV5Fhxvqvo3E-0oAvDCYR3ImsB_PYkxyWdWdXhTD5Y766tWIZwKKV9DchIlBlHmxzerQwiMecCJYAmcLB5pl4eS94Zka8_b5dpBluhUXATkBQKGqewO8k-4p5o_SVIXvBWUQqqRFQXWm4PuttgobAWFp9UfZ1KJRVFYjrXpUcUOpNQW0PHsBxBPeG871OK_KA_6gRbl5nqn-YEwmJfKt7GnedB1dS44nXBVluptbtkRkSm2eU3wS0deHKa2Ivf95nvrFvJUgsry1qmie7fKQAA")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2046092634").split()))
