USE sakila;

-- 1a --
SELECT first_name, last_name FROM actor;
-- 1b -
SELECT CONCAT( first_name, ',', last_name ) FROM actor AS Actor_Name;
-- 2a --
SELECT actor_id, first_name, last_name FROM actor WHERE first_name = 'Joe'; 
-- 2b --
SELECT actor_id, first_name, last_name FROM actor WHERE last_name LIKE '%GEN%';
-- 2c --
SELECT last_name, first_name FROM actor WHERE last_name LIKE '%LI%';	
-- 2d --
SELECT country_id, country FROM country WHERE country IN ('Afghanistan', 'Bangladesh', 'China');
-- 3a --
ALTER TABLE actor ADD COLUMN description BLOB;
-- 3b --
ALTER TABLE actor DROP COLUMN description;
-- 4a --
SELECT last_name, COUNT(last_name) FROM actor GROUP BY last_name;
-- 4b --
SELECT last_name, COUNT(last_name) FROM actor GROUP BY last_name HAVING COUNT(last_name) >= 2;
-- 4c --
UPDATE actor
SET 
    first_name = 'HARPO'
WHERE
    first_name = 'GROUCHO' AND last_name = 'WILLIAMS';
    
-- 4d -- 
UPDATE actor
SET 
    first_name = 'GROUCHO'
WHERE
    first_name = 'HARPO' AND last_name = 'WILLIAMS';
    
-- 5a --
SHOW CREATE TABLE address;
-- 6a --
SELECT s.first_name, s.last_name, a.address 
FROM staff s
INNER JOIN address a ON s.address_id = a.address_id;
-- 6b --
SELECT payment_date FROM payment;
SELECT s.first_name, s.last_name, p.amount 
FROM staff s
INNER JOIN payment p ON s.staff_id = p.staff_id
WHERE p.payment_date IN ('2005-08-01 08:51:04',
'2005-08-02 15:36:52',
'2005-08-02 18:01:38',
'2005-08-17 12:37:54',
'2005-08-18 03:57:29',
'2005-08-19 09:55:16',
'2005-08-19 13:56:54',
'2005-08-21 23:33:57',
'2005-08-22 01:27:57',
'2005-08-22 19:41:37',
'2005-08-22 20:03:46');
-- 6c --
SELECT f.title, COUNT(a.actor_id)
FROM film f
INNER JOIN film_actor a ON f.film_id = a.film_id
GROUP BY f.title;
-- 6d --
SELECT f.title, COUNT(i.film_id)
FROM film f
INNER JOIN inventory i ON f.film_id = i.film_id
WHERE f.title = 'Hunchback Impossible';
-- 6e --
SELECT c.last_name, c.first_name, SUM(p.amount)
FROM customer c
INNER JOIN payment p ON c.customer_id = p.customer_id
GROUP BY c.last_name;
-- 7a --
SELECT title 
FROM film
	WHERE language_id IN 
    (
    SELECT language_id 
    FROM language
    WHERE name = 'ENGLISH'
    )
    HAVING title LIKE 'K%' OR 'Q%';

-- 7b --
SELECT first_name, last_name
FROM actor
	WHERE actor_id IN 
    (
    SELECT actor_id
    FROM film_actor
    WHERE film_id IN
		(
		SELECT film_id
        FROM film
        WHERE title = 'Alone Trip'
        )
    );
    
-- 7c --
SELECT c.first_name, c.last_name, c.email
FROM customer c 
INNER JOIN country t ON c.last_update = t.last_update
WHERE t.country = 'Canada'; 
-- 7 d --
SELECT title
FROM film
WHERE film_id IN
(
	SELECT film_id
    FROM film_category
    WHERE category_id IN
    (
		SELECT category_id
        FROM category
        WHERE name = 'family'
	)
);

-- 7e --
SELECT title
FROM film
WHERE film_id IN 
	(
    SELECT film_id
    FROM inventory
    WHERE inventory_id IN 
    (
		SELECT inventory_id
        FROM rental
        GROUP BY rental_id DESC
        )
	);

-- 7f --
SELECT s.store_id, SUM(p.amount)
FROM payment p  
inner JOIN store s ON s.manager_staff_id = p.staff_id
GROUP BY s.store_id;
-- 7g --
SELECT s.store_id, c.city, t.country
FROM store s 
INNER JOIN address a  ON s.address_id = a.address_id
INNER JOIN city c ON a.city_id = c.city_id
INNER JOIN country t on c.country_id = t.country_id; 
-- 7h --
SELECT c.name, SUM(amount)
FROM category c 
INNER JOIN film_category f ON c.category_id = f.category_id
INNER JOIN inventory i ON f.film_id = i.film_id
INNER JOIN rental r ON i.inventory_id = r.inventory_id
INNER JOIN payment p ON p.customer_id = r.customer_id
GROUP BY c.name
ORDER BY SUM(amount) DESC
LIMIT 5;
-- 8a --
CREATE VIEW top_genres AS (
SELECT c.name, SUM(amount)
FROM category c 
INNER JOIN film_category f ON c.category_id = f.category_id
INNER JOIN inventory i ON f.film_id = i.film_id
INNER JOIN rental r ON i.inventory_id = r.inventory_id
INNER JOIN payment p ON p.customer_id = r.customer_id
GROUP BY c.name
ORDER BY SUM(amount) DESC
LIMIT 5
);

-- 8b --
SELECT name
FROM top_genres;
-- 8c --
DROP VIEW IF EXISTS sakila.top_genres;