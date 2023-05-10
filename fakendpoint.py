#!/usr/bin/env python3

import cgi
import sys


def bad_request():
    print('Status: 400 Bad Request')
    print("\n")
    sys.exit(0)


def int_error():
    print('Status: 500 Internal Server Error')
    print("\n")
    sys.exit(0)


if len(sys.argv) > 1:
    sys.exit(0)

form = cgi.FieldStorage()


if form.getvalue("path") is None:
    print("Content-type: text/html\n")
    print("\n")
    print('Missing filename')
    print("\n")
    bad_request
    sys.exit(0)
basedir = '/tmp'

fileitem = form['path']
f = open("%s/%s" % (basedir, fileitem.filename), 'wb')
f.write(fileitem.file.read())
f.close()

print("Status: 200 OK\n")
print("Content-type: text/html\n")
print("\n")

sys.exit(0)
