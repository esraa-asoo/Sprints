FROM mysql:latest
RUN chown -R mysql:mysql /docker-entrypoint-initdb.d/:ro
COPY ./MySQL_Queries /docker-entrypoint-initdb.d/:ro  