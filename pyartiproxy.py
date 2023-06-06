#!/usr/bin/env python3

import cgi
import configparser
import os
import requests
import sys


def int_error():
    print('Status: 500 Internal Server Error')
    print("\n")
    sys.exit(0)


config = configparser.ConfigParser()
try:
    config.read('/etc/pyartiproxy.ini')
except:
    int_error()

if "main" not in config:
    int_error()
if "default" not in config["main"]:
    int_error()

cfg_section = config["main"]["default"]
if "token" not in config[cfg_section]:
    int_error()
if "url" not in config[cfg_section]:
    int_error()
if "user" not in config[cfg_section]:
    int_error()

ARTI_TOKEN = config[cfg_section]["token"]
ARTI_URL = config[cfg_section]["url"]
ARTI_USER = config[cfg_section]["user"]

if len(sys.argv) > 1:
    sys.exit(0)

form = cgi.FieldStorage()

if form.getvalue("filename") is None:
    print("Content-type: text/html")
    print('Status: 400 Bad Request')
    print("\n")
    print('Missing filename')
    print("\n")
    sys.exit(0)

filename = form.getvalue("filename")
if len(filename) == 0:
    filename = "emptyfilename"
idx = filename.find('/')
filename.lstrip('\x00')
if idx != -1:
    print("Content-type: text/plain")
    print('Status: 400 Bad Request')
    print("\n")
    print(f'Filename have a / {filename}\n')
    print("\n")
    sys.exit(0)

# TODO validate [0-9a-zA-Z_-]*

basedir = "/var/www/html/"
basedir = "/tmp/"
if not os.path.isdir(basedir):
    try:
        os.makedirs(basedir)
    except:
        print("Content-type: text/html")
        print('Status: 400 Bad Request')
        print("\n")
        print('Bad directory')
        print("\n")
        sys.exit(0)

data = form.getvalue("data")
if data is None:
    print("Content-type: text/html")
    print('Status: 400 Bad Request')
    print("\n")
    print('Missing data')
    print("\n")
    sys.exit(0)

f = open(f"{basedir}/{filename}", 'wb')
f.write(data)
f.close()
try:
    f = open(f"{basedir}/{filename}", 'wb')
    f.write(data)
    f.close()
except:
    print("Content-type: text/html")
    print('Status: 400 Bad Request')
    print("\n")
    print(f'Fail to open {basedir}/{filename}XXX')
    print("\n")
    sys.exit(0)

print("Status: 200 OK\n")
print("Content-type: text/html\n")
print("\n")

headers = {
    "token": ARTI_TOKEN,
    }
files = {
    "path": (
        filename,
        open(f"{basedir}/{filename}", 'rb')
        )
}
url = ARTI_URL + "/artifacts/home/agl"
r = requests.post(url, data=headers, files=files)
print(r)
print(r.text)
print(r.headers)

sys.exit(0)
