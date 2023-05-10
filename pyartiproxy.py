#!/usr/bin/env python3

import cgi
import configparser
import os
import requests
import sys


def bad_request():
    print('Status: 400 Bad Request')
    print("\n")
    sys.exit(0)


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
    print("Content-type: text/html\n")
    print("\n")
    print('Missing filename')
    print("\n")
    bad_request
    sys.exit(0)

basedir = "/var/www/html/"
if not os.path.isdir(basedir):
    try:
        os.makedirs(basedir)
    except:
        print("Content-type: text/html\n")
        print("\n")
        print('Bad directory')
        print("\n")
        bad_request
        sys.exit(0)

f = open("%s/%s" % (basedir, form.getvalue("filename")), 'wb')
f.write(form.getvalue("data"))
f.close()
print("Status: 200 OK\n")
print("Content-type: text/html\n")
print("\n")

headers = {
    "token": ARTI_TOKEN,
    }
files = {
    "path": (
        form.getvalue("filename"),
        open("%s/%s" % (basedir, form.getvalue("filename")), 'rb')
        )
}
url = ARTI_URL + "/artifacts/home/agl"
r = requests.post(url, data=headers, files=files)
print(r)
print(r.text)
print(r.headers)

sys.exit(0)
