import os
from dotenv import load_dotenv


# create database file 
if not os.path.exists('./DB.db'):
    with open('DB.db', 'w+') as db:
        pass
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

# lang status
RU = 0
EN = 1
