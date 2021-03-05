import os
import socket
from ssh2.session import Session
import ssh2

host = 'localhost'
user = "root"
passw = "shail$"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, 22))
session = Session()
session.handshake(sock)
session.userauth_password(user, passw)

channel = session.open_session()
channel.execute('echo me')
size, data = channel.read()
while size > 0:
    print(data)
    size, data = channel.read()
channel.close()
print("Exit status: %s" % channel.get_exit_status())