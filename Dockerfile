FROM debian:buster

RUN apt-get update && apt-get -y install apache2 python3 python3-requests
RUN a2dismod mpm_event
RUN a2enmod mpm_prefork
RUN a2enmod cgi
RUN a2enconf serve-cgi-bin
COPY pyartiproxy.py /usr/lib/cgi-bin/
RUN chmod 755 /usr/lib/cgi-bin/pyartiproxy.py
RUN chown www-data /var/www/html

COPY pyartiproxy.ini /etc
COPY run.sh /
CMD /run.sh
