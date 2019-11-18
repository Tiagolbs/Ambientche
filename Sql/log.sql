-- Database: LogTest

-- DROP DATABASE "LogTest";

CREATE DATABASE "LogTest"
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Portuguese_Brazil.1252'
    LC_CTYPE = 'Portuguese_Brazil.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;
	
CREATE SEQUENCE id_seq
	INCREMENT 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	START 1
	CACHE 1;
	
CREATE TABLE LogStatusLuz(
	id int primary key DEFAULT nextval('id_seq') NOT NULL,
	dt_data varchar(50),
	comodo int,
    status bool
)
