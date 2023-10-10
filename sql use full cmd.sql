-- all use full command in sql 


-- SELECT * FROM products;
-- SELECT * FROM products ORDER BY id;
-- SELECT id AS products_id, is_sale AS on_sale from products;
-- SELECT id, name, is_sale, price FROM products WHERE id = 5;
-- SELECT * FROM products WHERE id = 6;
-- SELECT * FROM products WHERE inventory = 12;
-- SELECT * FROM products WHERE name = 'Remote';
-- SELECT * FROM products WHERE price >= 250;
-- SELECT * FROM products WHERE inventory != 20;
-- SELECT * FROM products WHERE inventory <> 12;
-- SELECT * FROM products WHERE price >= 0 AND price <= 25000;
-- SELECT * FROM products WHERE inventory >= 20 AND price <= 250;
-- SELECT * FROM products WHERE id = 6 OR id = 7 OR id = 8;
-- SELECT * FROM products WHERE id IN (6,7,8,9);
-- SELECT * FROM products WHERE name LIKE 'AC%';
-- SELECT * FROM products WHERE name LIKE '%e';
-- SELECT * FROM products WHERE name NOT LIKE '%AC%';
-- SELECT * FROM products ORDER BY price ASC;
-- SELECT * FROM products ORDER BY inventory DESC, price;
-- SELECT * FROM products WHERE price > 250 ORDER BY created_at DESC;
-- SELECT * FROM products ORDER BY id DESC LIMIT 5;
-- SELECT * FROM products WHERE price <= 4500 LIMIT 3;
-- SELECT * FROM products ORDER BY price LIMIT 5;
-- SELECT * FROM products ORDER BY id  LIMIT 5 OFFSET 2;
-- INSERT INTO products (price, name, inventory) VALUES (72000,'Laptop', 4), (300, 'Mouse', 3), (1500000, 'CPU', 2) returning *;
-- SELECT * FROM products WHERE name = 'Tshirt';
-- DELETE FROM products WHERE id = 28 returning *;
-- DELETE FROM products WHERE inventory = 0 returning *;
-- UPDATE products SET name = 'Chicken shirt', price = 599 WHERE id = 20 returning *;
-- UPDATE products SET is_sale = false WHERE id < 15 returning *;
-- select count(*) from updatequestion WHERE subject_id = 5;

-- SELECT subject_id AS ID, answer AS ans FROM updatequestion;
-- SELECT * FROM updatequestion
-- SELECT question, CONCAT(option_a,', ',option_b,', ',option_c,', ',option_d) AS answer FROM updatequestion;
-- select *  from updatequestion order by id
-- SELECT subject FROM crud UNION SELECT question FROM updatequestion order by subject;
-- SELECT name FROM products UNION ALL SELECT question FROM updatequestion order by name;
-- SELECT price, inventory FROM products WHERE price='45000' UNION SELECT price, inventory FROM products WHERE price='45000' ORDER BY price;
-- SELECT COUNT(name), price FROM products GROUP BY price;
-- SELECT COUNT(answer), option_c FROM updatequestion GROUP by option_c;
-- SELECT COUNT(answer), option_c FROM updatequestion GROUP BY option_c ORDER BY COUNT(answer);
-- SELECT COUNT(answer), option_c FROM updatequestion GROUP BY option_c HAVING COUNT(answer) < 1;
-- SELECT COUNT(answer), option_c FROM updatequestion GROUP BY option_c HAVING COUNT(answer) < 25 ORDER BY COUNT(answer) DESC;



-- The percent sign (%) represents zero, one, or multiple characters
-- The underscore sign (_) represents one, single character