SELECT * FROM seminar1.student;

/*
SELECT first_name, email FROM student
WHERE first_name LIKE "A%"
*/

SELECT first_name, email FROM student
WHERE first_name LIKE "%A%";

CREATE DATABASE work;
USE work;
CREATE TABLE worker
(
id INT PRIMARY KEY NOT NULL,
name_worker VARCHAR(30) NOT NULL,
dept VARCHAR(30) NOT NULL,
salary INT
);

SELECT * FROM worker;

INSERT worker(id, name_worker, dept, salary)
VALUES
(100, 'AndreyEX', 'Sales', 	5000),
(200, 'Boris', 'IT', 5500),
(300, 'Anna', 'IT', 3000),
(400, 'Anton', 'Marketing', 9500),
(500, 'Haron', 'IT', 3000),
(501, 'Parom', 'Sales', NULL);

/*
SELECT * FROM worker
WHERE salary > 6000;
*/

/*
SELECT * FROM worker
WHERE dept = 'IT';
*/
/*
SELECT * FROM worker
WHERE dept != 'IT';
*/









