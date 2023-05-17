-- script to create database hbtn_0d_usa and tables states
-- creates database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use a database
USE hbtn_0d_usa;
-- create table 
CREATE TABLE IF NOT EXISTS states(id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
