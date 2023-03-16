## Login
```
sudo mysql -u root -p
```
## Create Database
```
CREATE DATABASE [name-of-database];
```
## Create a user
```
CREATE USER 'exampleuser'@'localhost' IDENTIFIED BY 'password';
```
## Grant Privileges
```
GRANT ALL PRIVILEGES ON [name-of-database].* TO 'exampleuser'@'localhost' IDENTIFIED BY 'password';
```
## Flush the Privileges
```
FLUSH PRIVILEGES;
```
## Quit out
```
quit;
```
## Connect to SQL user
```
mysql -u exampleuser -p
```
## Modify [name-of-database]
```
USE [name-of-database];
```
## Create table
```
CCREATE TABLE exampleTable (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(225) NOT NULL,
  due_date DATE
) ENGINE=INNODB;
```
## Insert data into the new table
```
INSERT INTO exampleTable (title, due_date) VALUES ('MYSQL On The Pi', now());
```
## Grab all data from table
```
SELECT * FROM exampleTable;
```
