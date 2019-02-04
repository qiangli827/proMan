import os
from dotenv import load_dotenv

dotenv_path = path = 'C:\\Users\\orangebox\\OneDrive\\document\\flask\\projects\\proMan\\.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# import sys
# path = 'C:\\Users\\orangebox\\OneDrive\\document\\flask\\projects\\proMan\\proMan'
# if path not in sys.path:
#    sys.path.insert(0, path)

from proMan import app as application
