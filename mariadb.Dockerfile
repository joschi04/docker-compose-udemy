FROM mariadb:10.3

ENV MYSQL_ROOT_PASSWORD=root

COPY docker.sql /docker-entrypoint-initdb.d/