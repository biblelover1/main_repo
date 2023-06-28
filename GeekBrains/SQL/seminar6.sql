USE lesson5;

DROP PROCEDURE hello;
delimiter //
CREATE PROCEDURE hello()
	BEGIN
		CASE
			WHEN CURTIME() BETWEEN '06:00:00' AND '11:59:59' THEN
            SELECT 'Доброе утро';
            WHEN CURTIME() BETWEEN '12:00:00' AND '17:59:59' THEN
            SELECT 'Добрый день';
            WHEN CURTIME() BETWEEN '18:00:00' AND '23:59:59' THEN
            SELECT 'Добрый вечер' AS 'Время';
            ELSE
            SELECT 'Доброй ночи';
		END CASE;
	END //
delimiter ;

CALL hello();


delimiter //
CREATE FUNCTION fibonacci(num INT) -- Колво чисел Фибоначчи для вывода 
RETURNS VARCHAR(50)
DETERMINISTIC
BEGIN
DECLARE fib1 INT DEFAULT 0;
DECLARE fib2 INT DEFAULT 1; 
DECLARE fib3 INT DEFAULT 0;
DECLARE result VARCHAR(50) DEFAULT '0 1';
IF num = 1 THEN
RETURN fib1;
ELSEIF num = 2 THEN
RETURN CONCAT(fib1, ' ', fib2);
ELSE
WHILE num > 2
DO
SET fib3 = fib1 + fib2;
SET fib1 = fib2;
SET fib2 = fib3;
SET num = num - 1;
SET result = CONCAT(result, ' ', fib3);
END WHILE;
RETURN result;
END IF;
END //
delimiter ;

SELECT fibonacci(7);
SELECT fibonacci(5);

/*Создайте и вызовите процедуру, которая при ее вызове будет выводить:
«Однозначное число» - если ее параметр равен от 1 до 9
«Двухзначное число» - если ее параметр равен от 10 до 99
«Трехзначное число» - если ее параметр равен от 100 до 999
*/

delimiter //
CREATE PROCEDURE pr2(num INT)
BEGIN
CASE
WHEN num > 0  AND num < 10 THEN
SELECT 'однозначное';
WHEN num > 9  AND num < 99 THEN
SELECT 'двузначное';
ELSE
SELECT 'трехзначное';
END CASE;
END //
delimiter ;

CALL pr2(100);


-- Создайте функцию которая будет вычислять сумму трех переменных
-- a = 2030, b = 5124, c = 7903.


DROP FUNCTION pt;
delimiter $$
CREATE FUNCTION pt2() 
RETURNS INT
DETERMINISTIC
BEGIN
DECLARE a INT DEFAULT 2030; -- fib1 = 0
DECLARE b INT DEFAULT 5124; -- fib2 = 1
DECLARE c INT DEFAULT 7903; -- fib3 = 0
DECLARE result INT ;

SET result = a+b+c;
RETURN result;
END $$
delimiter ;

SELECT pt();

DROP TABLE bankaccounts;
CREATE TABLE bankaccounts(accountno varchar(20) PRIMARY KEY NOT NULL, funds decimal(8,2));

INSERT INTO bankaccounts VALUES("ACC1", 1000);
INSERT INTO bankaccounts VALUES("ACC2", 1000);

SELECT * FROM bankaccounts;

UPDATE bankaccounts
SET funds = funds + 100
WHERE accountno = 'ACC1';

START TRANSACTION;
UPDATE bankaccounts
SET funds = funds - 100
WHERE accountno = 'ACC1';
UPDATE bankaccounts
SET funds = funds + 100
WHERE accountno = 'ACC2';
TRUNCATE bankaccounts;

START TRANSACTION;
UPDATE bankaccounts
SET funds = funds - 100
WHERE accountno = 'ACC1';
UPDATE bankaccounts
SET funds = funds + 100
WHERE accountno = 'ACC2';
ROLLBACK;

START TRANSACTION;
UPDATE bankaccounts
SET funds = funds - 100
WHERE accountno = 'ACC1';
UPDATE bankaccounts
SET funds = funds + 100
WHERE accountno = 'ACC2';
COMMIT;