
# BUILD WITH
# docker build --secret id=db_secret,src=./db_secret -t foon-db:latest .

FROM postgres:latest

ENV PGDATA = "/var/lib/postgresql/data/pgdata"

VOLUME ["/var/lib/postgresql/data"]

COPY foon_schema_create.sql /docker-entrypoint-initdb.d/
EXPOSE 5432



