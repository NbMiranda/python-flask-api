FROM mysql:5.7
ENV MYSQL_ROOT_PASSWORD=password
VOLUME [ "/var/lib/mysql" ]
EXPOSE 3306:3306