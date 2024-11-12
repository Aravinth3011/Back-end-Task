It's a GUI project using python tkinter and MySQL database.

Make sure you already have installed all the modules used in this project. Please see the requirement.txt file for all the requirements.


Steps to follow after installing all the modules. Otherwise this application will not work properly.

->Create a database with this name, "userdata"
->create a table with this name, "data"


USE this code to create the table under the "userdata" database

create table student_register(
   id INT(225) NOT NULL AUTO_INCREMENT,
   email VARCHAR(225) NOT NULL,
   username VARCHAR(225) NOT NULL,
   password VARCHAR(225) NOT NULL,
);
