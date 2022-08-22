import os
from dotenv import load_dotenv

# create dir for voice messages
if not os.path.exists('./tmp'):
    os.mkdir('./tmp')
# create dir for logs
if not os.path.exists('./logs'):
    os.mkdir('./logs')

# load env varibale
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# Bot token
TOKEN = os.getenv('TOKEN')


