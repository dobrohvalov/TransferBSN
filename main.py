import uuid
import conf

import smbclient
from smbprotocol.connection import Connection, Dialects

try:
    connection = Connection(uuid.uuid4(), server_name=str(conf.SMB_server), port=conf.SMB_port)
    connection.connect(Dialects.SMB_3_0_2)
    print("OK")
except Exception as e:
    print(e)

try:
    smbclient.ClientConfig(username=conf.SMB_login, password=conf.SMB_password)
    print('OK')
except Exception as e:
    print(e)
