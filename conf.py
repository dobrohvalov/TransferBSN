import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

file_source = os.getenv('FILE_SOURCE')  # Source from which we will take files
file_destination = os.getenv('FILE_DESTINATION')  # File transfer point
amount_days = os.getenv('AMOUNT_DAYS')  # How many days to transfer files
SMB_login = os.getenv('SMB_LOGIN')  # login of SMB protocol
SMB_password = os.getenv('SMB_PASSWORD')  # password of SMB protocol
SMB_server = os.getenv('SMB_SERVER')  # ip of server smp
SMB_port = os.getenv('SMB_port')
