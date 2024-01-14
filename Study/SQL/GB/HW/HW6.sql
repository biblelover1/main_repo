-- HOMEWORK
-- Создайте функцию, которая принимает кол-во сек и формат их в кол-во дней часов. Пример: 123456 ->'1 days 10 hours 17 minutes 36 seconds'
USE lesson_5;
DELIMITER //
DROP FUNCTION IF EXISTS sec_in_days;
CREATE FUNCTION sec_in_days(num INT)
RETURNS VARCHAR(50)
DETERMINISTIC
BEGIN
    DECLARE seconds INT;
    DECLARE minutes INT;
    DECLARE hours INT;
    DECLARE days INT;
    DECLARE result VARCHAR(50);
    
    SET seconds = (num % 60) % 60;
    SET minutes = ((num DIV 60) % 60) % 60;
    SET hours = (((num DIV 60) DIV 60) % 24) % 60;
    SET days = (((num DIV 60) DIV 60) DIV 24);
    
    SET result = CONCAT(days, ' days, ', hours, ' hours, ', minutes, ' minutes, ', seconds, ' seconds');
    
    RETURN result;
END //
DELIMITER ;
SELECT sec_in_days(123456);



/*
Создайте процедуру которая, выводит только четные числа от 1 до 10. Пример: 2,4,6,8,10
*/
USE lesson_5;

DELIMITER //
CREATE PROCEDURE get_even_numbers(IN num INT)
BEGIN
    DECLARE i INT DEFAULT num;
    DECLARE even_num INT;
    PREPARE stmt FROM 'SELECT ? INTO @even_num';
    WHILE i <= 10 DO
        IF i % 2 = 0 THEN
            SET @even_num = i;
            EXECUTE stmt USING @even_num;
            SELECT @even_num as 'Even Numbers';
        END IF;
        SET i = i + 1;
    END WHILE;
END //
DELIMITER ;
CALL get_even_numbers(3);