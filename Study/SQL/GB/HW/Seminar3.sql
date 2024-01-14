DROP DATABASE IF EXISTS Seminar3;
CREATE DATABASE IF NOT EXISTS Seminar3;

USE Seminar3;
DROP table IF EXISTS `staff`;
CREATE table IF NOT EXISTS `staff`
(
`id` INT PRIMARY KEY AUTO_INCREMENT,
`firstname` VARCHAR(45),
`lastname` VARCHAR(45),
`post` VARCHAR(45),
`seniority` INT,
`salary` INT,
`age` INT);

INSERT INTO `staff` (`firstname`, `lastname`, `post`,`seniority`,`salary`, `age`)
VALUES
('Вася', 'Васькин', 'Начальник', 40, 100000, 60), 
('Петр', 'Власов', 'Начальник', 8, 70000, 30),
('Катя', 'Катина', 'Инженер', 2, 70000, 25),
('Саша', 'Сасин', 'Инженер', 12, 50000, 35),
('Иван', 'Петров', 'Рабочий', 40, 30000, 59),
('Петр', 'Петров', 'Рабочий', 20, 55000, 60),
('Сидр', 'Сидоров', 'Рабочий', 10, 20000, 35),
('Антон', 'Антонов', 'Рабочий', 8, 19000, 28),
('Юрий', 'Юрков', 'Рабочий', 5, 15000, 25),
('Максим', 'Петров', 'Рабочий', 2, 11000, 19),
('Юрий', 'Петров', 'Рабочий', 3, 12000, 24),
('Людмила', 'Маркина', 'Уборщик', 10, 10000, 49);

DROP TABLE IF EXISTS `activity_staff`;
CREATE TABLE IF NOT EXISTS `activity_staff`
(
`id` INT PRIMARY KEY AUTO_INCREMENT,
`staff_id` INT, FOREIGN KEY(staff_id) REFERENCES staff(id),
`date_activity` DATE,
`count_pages` INT
);

INSERT activity_staff (`staff_id`, `date_activity`, `count_pages`)
VALUES
(1,'2022-01-01',250),
(2,'2022-01-01',220),
(3,'2022-01-01',170),
(1,'2022-01-02',100),
(2,'2022-01-01',220),
(3,'2022-01-01',300),
(7,'2022-01-01',350),
(1,'2022-01-03',168),
(2,'2022-01-03',62),
(3,'2022-01-03',84);

-- Средняя зарплата по фирме
SELECT AVG(salary)
FROM staff;

-- Вывести зарплату сотрудников, у которых зарплата выше средней
SELECT * FROM staff
WHERE salary > (SELECT AVG(salary) FROM staff);

-- ЗП сортировка от меньшего к большему
SELECT * FROM staff
ORDER BY salary; -- ASC - defolt

-- ЗП сортировка по убыванию
SELECT * FROM staff
ORDER BY salary DESC; 

-- Получить инф-ию о ЗП сотрудниках, должность = рабочий, стаж = >5 лет

 SELECT salary, id, post, seniority FROM staff
 WHERE seniority > 5 AND post = "Рабочий"
 ORDER BY seniority;
 
 -- Все записи в staff по age(ASC)
SELECT * FROM staff
ORDER BY age;

-- SORTING firstname
SELECT * FROM staff
ORDER BY firstname;

-- 
SELECT firstname, lastname, age FROM staff
ORDER BY firstname DESC;

-- 
SELECT * FROM staff
ORDER BY firstname DESC, age DESC;

-- Count workers by lastname
SELECT COUNT(lastname)
FROM staff;

SELECT * FROM staff
ORDER BY lastname;

-- Count of unique lastnames
SELECT COUNT(DISTINCT lastname)
FROM staff;

-- First five rows
SELECT id, firstname FROM staff
LIMIT 5;

-- First five rows after first worker
SELECT id, firstname FROM staff
LIMIT 1, 6; -- пропуск 1 строки


-- unique firstnames 
SELECT COUNT(DISTINCT firstname) FROM staff;

-- 
SELECT id FROM staff
ORDER BY id
LIMIT 2;

-- 
SELECT id FROM staff
ORDER BY id
LIMIT 4, 3;

--
SELECT id FROM staff
ORDER BY id DESC
LIMIT 2, 3;

-- group workers by post + max min salary 
SELECT SUM(salary) "Сумма зарплат должности", COUNT(lastname) "Количество сотрудников в каждой должности", post,
MAX(salary) "MAX salary by post",
MIN(salary) "MIN salary by post",
MAX(salary) - MIN(salary) "Difference in salary"
FROM staff
GROUP BY post;

SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));

-- 
SELECT staff_id, SUM(count_pages) FROM activity_staff
GROUP BY staff_id;

-- 
SELECT date_activity, SUM(count_pages) FROM activity_staff
GROUP BY date_activity;

--
SELECT date_activity, AVG(count_pages) FROM activity_staff
GROUP BY date_activity;

--
SELECT name_age, SUM(salary)
FROM (SELECT salary,
	CASE
		WHEN age < 20 THEN "1 group"
		WHEN age > 20 AND age < 40 THEN "2 group"
		WHEN age > 40 THEN "3 group"
        ELSE "Group undefined"
	END as name_age
FROM staff) as querry1
GROUP BY name_age;

-- 
SELECT staff_id, SUM(count_pages) AS `All pages`
FROM activity_staff
GROUP BY staff_id
HAVING `All pages` > 500;

--
SELECT date_activity, COUNT(DISTINCT staff_id) as `count`
FROM activity_staff
GROUP BY date_activity
HAVING `count` > 3;

--
SELECT post, AVG(salary) as `AVG` FROM staff
GROUP BY post
HAVING `AVG` > 30000

