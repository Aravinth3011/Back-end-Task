It's a GUI project using python tkinter and MySQL database.

->Create a database with this name, "userdata"
->create a table with this name, "data"


USE this code to create the table under the "userdata" database

create table student_register(
   id INT(225) NOT NULL AUTO_INCREMENT,
   email VARCHAR(225) NOT NULL,
   username VARCHAR(225) NOT NULL,
   password VARCHAR(225) NOT NULL,
);
