USE lesson5;
DROP TABLE IF EXISTS cars;
CREATE TABLE cars
(
	id INT NOT NULL PRIMARY KEY,
    name VARCHAR(45),
    cost INT
);

INSERT cars
VALUES
	(1, "Audi", 52642),
    (2, "Mercedes", 57127 ),
    (3, "Skoda", 9000 ),
    (4, "Volvo", 29000),
	(5, "Bentley", 350000),
    (6, "Citroen ", 21000 ), 
    (7, "Hummer", 41400), 
    (8, "Volkswagen ", 21600);
    
SELECT *
FROM cars;

-- HOMEWORK
-- Создайте представление, в которое попадут автомобили стоимостью до 25 000 долларов
DROP VIEW IF EXISTS low_cost_cars;
CREATE VIEW low_cost_cars AS
SELECT 
name, cost 
FROM cars
WHERE cost < 25000;

SELECT * FROM low_cost_cars;

-- Изменить в существующем представлении порог для стоимости: пусть цена будет до 30 000 долларов (используя оператор ALTER VIEW)
ALTER VIEW low_cost_cars AS
SELECT name, cost
FROM cars
WHERE cost < 30000;

SELECT * FROM low_cost_cars;

-- Создайте представление, в котором будут только автомобили марки “Шкода” и “Ауди” (аналогично)

DROP VIEW IF EXISTS V_A_cars;
CREATE OR REPLACE VIEW V_A_cars AS
SELECT name, cost
FROM cars
WHERE name = 'Skoda' OR name = 'Audi';

SELECT * FROM V_A_cars;

-- Получить ранжированный список автомобилей по цене в порядке возрастания

SELECT id, name, cost
FROM cars
ORDER BY cost;

-- Получить топ-3 самых дорогих автомобилей, а также их общую стоимость

SELECT SUM(cost) `exp_cars_cost`
FROM (SELECT id, name, cost
FROM cars 
ORDER BY cost DESC
LIMIT 3) `top3`;

-- Получить список автомобилей, у которых цена больше предыдущей цены (т.е. у которых произошло повышение цены)
DROP VIEW IF EXISTS cost_diff;
CREATE OR REPLACE VIEW cost_diff AS
SELECT id, name, cost,
LEAD(cost) OVER(ORDER BY id) `lead`,
LAG(cost) OVER(ORDER BY id) `lag`
FROM cars;

SELECT id, name, cost, `lead`, `lag`
FROM cost_diff
WHERE cost - `lag` > 0;

-- Получить список автомобилей, у которых цена меньше следующей цены (т.е. у которых произойдет снижение цены)

DROP VIEW IF EXISTS price_diff;
CREATE OR REPLACE VIEW price_diff AS
SELECT id, name, cost,
LEAD(cost) OVER(ORDER BY id) `lead`,
LAG(cost) OVER(ORDER BY id) `lag`
FROM cars;

SELECT id, name, cost
FROM cost_diff
WHERE cost - `lag` < 0;

/* 
Получить список автомобилей, отсортированный по возрастанию цены, 
и добавить столбец со значением разницы между текущей ценой и ценой следующего автомобиля
*/
DROP VIEW IF EXISTS new_diff;
CREATE OR REPLACE VIEW new_diff AS
SELECT id, name, cost,
LEAD(cost) OVER o `lead`,
LAG(cost) OVER o `lag`,
LEAD(cost) OVER o - cost AS price_diff
FROM cars
WINDOW o AS (ORDER BY cost); 

SELECT name, cost, `lead`, `lag`, price_diff FROM new_diff;