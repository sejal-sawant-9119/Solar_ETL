1) GROUP BY & ORDER BY

SELECT signup_date, COUNT(*) AS num_users
FROM users
GROUP BY signup_date
ORDER BY signup_date;

2) JOIN

SELECT c.customer_name, SUM(o.amount) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_name;


