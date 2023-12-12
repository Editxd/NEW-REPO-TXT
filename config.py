import os

API_ID = API_ID = 23539681

API_HASH = os.environ.get("API_HASH", "ae1430184ae21aa81b4b030d1bd75885")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6877438713:AAEaQe_NI39L9kHan32sJ5TwA34_CPnHOzA")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 1476002847))

LOG = -1002003879696

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1476002847").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


