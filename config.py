import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7629729778:AAHWOR4xC-pAx4Aa5vxntYTioqzT954AlT8")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "24411749"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "dccbce0579957e4ef718e31989b542da")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6981330984"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
