# Postgre Database creation Command
CREATE DATABASE market;
CREATE USER admin WITH PASSWORD 'pass';

ALTER ROLE admin SET client_encoding TO 'utf8';
ALTER ROLE admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE admin SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE market TO admin;



background from https://www.toptal.com/designers/subtlepatterns/
icons from flaticon and fontawesome


