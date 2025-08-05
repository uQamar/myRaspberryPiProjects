import platform
import socket
import os

print("Hostname:", socket.gethostname())
print("Architecture:", platform.machine())
print("OS:", platform.platform())
print("Running on:", os.uname().nodename)