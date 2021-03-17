#!/bin/sh

/etc/init.d/apache2 start

sleep 4

tail -F /var/log/apache2/*log
