import os
from dotenv import load_dotenv


if not os.path.exists('./tmp'):
    os.mkdir('./tmp')

# load env varibale
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# absolute path to bot dir 
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

# Bot token
TOKEN = os.getenv('TOKEN')


