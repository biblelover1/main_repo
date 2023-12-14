/*
Схема БД состоит из четырех таблиц:
Product(maker, model, type)
PC(code, model, speed, ram, hd, cd, price)
Laptop(code, model, speed, ram, hd, price, screen)
Printer(code, model, color, type, price)
Таблица Product представляет производителя (maker), номер модели (model) и тип ('PC' - ПК, 'Laptop' - ПК-блокнот или 'Printer' - принтер). Предполагается, что номера моделей в таблице Product уникальны для всех производителей и типов продуктов. В таблице PC для каждого ПК, однозначно определяемого уникальным кодом – code, указаны модель – model (внешний ключ к таблице Product), скорость - speed (процессора в мегагерцах), объем памяти - ram (в мегабайтах), размер диска - hd (в гигабайтах), скорость считывающего устройства - cd (например, '4x') и цена - price (в долларах). Таблица Laptop аналогична таблице РС за исключением того, что вместо скорости CD содержит размер экрана -screen (в дюймах). В таблице Printer для каждой модели принтера указывается, является ли он цветным - color ('y', если цветной), тип принтера - type (лазерный – 'Laser', струйный – 'Jet' или матричный – 'Matrix') и цена - price.
*/
-- Найдите номера моделей и цены всех имеющихся в продаже продуктов (любого типа) производителя B (латинская буква).

SELECT Product.model, price
FROM Product
INNER JOIN 
(SELECT model, price
FROM PC
UNION
SELECT model, price
FROM Laptop
UNION
SELECT model, price
FROM Printer) as Products
ON Product.model = Products.model
WHERE Product.maker = 'B'

-- Найдите производителя, выпускающего ПК, но не ПК-блокноты.
SELECT DISTINCT Product.maker
FROM Product 
WHERE type <> 'Printer'
EXCEPT
SELECT DISTINCT Product.maker
FROM Product WHERE type = 'Laptop'

--Найдите производителей ПК с процессором не менее 450 Мгц. Вывести: Maker
SELECT DISTINCT Product.maker
FROM Product 
INNER JOIN PC
ON Product.model = PC.model
WHERE PC.speed >= 450
 
--Найдите модели принтеров, имеющих самую высокую цену. Вывести: model, price
SELECT model, price
FROM Printer
WHERE price = (SELECT MAX(price) FROM Printer)

--Найдите размеры жестких дисков, совпадающих у двух и более PC. Вывести: HD
SELECT hd FROM PC
GROUP BY hd
HAVING COUNT(hd) > 1

--Найдите модели ПК-блокнотов, скорость которых меньше скорости каждого из ПК. Вывести: type, model, speed
SELECT DISTINCT type, Laptop.model, speed
FROM Laptop, Product
WHERE speed < ALL (SELECT speed FROM PC)
AND type = 'Laptop'

--Для каждого производителя, имеющего модели в таблице Laptop, найдите средний размер экрана выпускаемых им ПК-блокнотов. Вывести: maker, средний размер экрана.
SELECT maker, AVG(Laptop.screen)
FROM Product
INNER JOIN Laptop
ON Product.model = Laptop.model
WHERE Product.type = 'Laptop'
Group BY maker

--Найдите производителей, выпускающих по меньшей мере три различных модели ПК. Вывести: Maker, число моделей ПК.
SELECT DISTINCT maker, COUNT(model) as Count_Model FROM PRoduct
WHERE type = 'PC'
GROUP BY maker
HAVING COUNT(model) >= 3

--Найдите максимальную цену ПК, выпускаемых каждым производителем, у которого есть модели в таблице PC. Вывести: maker, максимальная цена.

SELECT maker, MAX(price) as Max_price
FROM Product
INNER JOIN PC
ON Product.model = PC.model
WHERE Product.type = 'PC'
GROUP BY maker

-- Для каждого значения скорости ПК, превышающего 600 МГц, определите среднюю цену ПК с такой же скоростью. Вывести: speed, средняя цена.
SELECT speed, AVG(price) as Avg_price
FROM PC
WHERE speed > 600
GROUP BY speed;

--Найдите производителей, которые производили бы как ПКсо скоростью не менее 750 МГц, так и ПК-блокноты со скоростью не менее 750 МГц. Вывести: Maker
SELECT maker
FROM Product
INNER JOIN PC
ON Product.model = PC.model
WHERE PC.speed >= 750
INTERSECT
(SELECT maker
FROM Product
INNER JOIN Laptop
ON Product.model = Laptop.model
WHERE Laptop.speed >= 750)

--Перечислите номера моделей любых типов, имеющих самую высокую цену по всей имеющейся в базе данных продукции.
SELECT model FROM 
(SELECT model, price FROM PC
UNION
SELECT model, price FROM Laptop
Union
SELECT model, price FROM Printer) as products
WHERE price = (SELECT MAX(price) 
FROM 
(SELECT model, price FROM PC
UNION
SELECT model, price FROM Laptop
Union
SELECT model, price FROM Printer) as products)

--Найдите производителей принтеров, которые производят ПК с наименьшим объемом RAM и с самым быстрым процессором среди всех ПК, имеющих наименьший объем RAM. Вывести: Maker

SELECT DISTINCT maker
FROM Product 
WHERE type = 'printer' AND 
      maker IN(SELECT maker 
               FROM Product 
               WHERE model IN(SELECT model 
                              FROM PC
                              WHERE speed = (SELECT MAX(speed)
                                             FROM (SELECT speed 
                                                   FROM PC 
                                                   WHERE ram=(SELECT MIN(ram)
                                                              FROM PC
                                                              )
                                                   ) AS z4
                                             )
                              )
               );

-- Используя таблицу Product, определить количество производителей, выпускающих по одной модели.
select count(maker)
from product
where maker in
(
  Select maker from product
  group by maker
  having count(model) = 1
)

--В предположении, что приход и расход денег на каждом пункте приема фиксируется не чаще одного раза в день [т.е. первичный ключ (пункт, дата)], написать запрос с выходными данными (пункт, дата, приход, расход). Использовать таблицы Income_o и Outcome_o.
SELECT t1.point, t1.date, inc, out
FROM income_o t1 LEFT JOIN outcome_o t2 ON t1.point = t2.point
AND t1.date = t2.date
UNION
SELECT t2.point, t2.date, inc, out
FROM income_o t1 RIGHT JOIN outcome_o t2 ON t1.point = t2.point
AND t1.date = t2.date

--В предположении, что приход и расход денег на каждом пункте приема фиксируется произвольное число раз (первичным ключом в таблицах является столбец code), требуется получить таблицу, в которой каждому пункту за каждую дату выполнения операций будет соответствовать одна строка. Вывод: point, date, суммарный расход пункта за день (out), суммарный приход пункта за день (inc). Отсутствующие значения считать неопределенными (NULL).
SELECT point, date, SUM(sum_out), SUM(sum_inc) FROM
(SELECT point, date, SUM(inc) as sum_inc, null as sum_out FROM Income
Group by point, date
UNION
SELECT point, date, null as sum_inc, SUM(out) as sum_out FROM Outcome
GROUP by point, date) as t
Group BY point, date
Order BY date

--Найдите средний размер диска ПК каждого из тех производителей, которые выпускают и принтеры. Вывести: maker, средний размер HD.
SELECT maker, AVG(hd) FROM PC
INNER JOIN Product 
ON PRODUCT.model = PC.model
WHERE maker in (SELECT maker FROM PRODUCT WHERE type = 'Printer')
GROUP BY maker