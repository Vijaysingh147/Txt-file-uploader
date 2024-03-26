import os

API_ID = API_ID = 23004101

API_HASH = os.environ.get("API_HASH", "a2e157e87728053027cbb156e41a832a")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6539249772:AAFUzL7ko9cnC4fyQ-2XyvEglXWPN0D0ix8")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5409975736))

LOG = -1002036952917,

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5409975736").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


