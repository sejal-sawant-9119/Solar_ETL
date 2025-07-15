# Solar ETL Pipeline (Day 0)

🚀 **Goal:**  
This is my starter project to build foundational Data Engineering skills.  
It uses a simple solar operations dataset to practice cleaning data, loading into a database, and running SQL queries.

---

## ✅ What this project does

- Loads raw CSV data using Python pandas.
- Cleans missing values and standardizes dates.
- Adds a new `year` column for analysis.
- Saves cleaned data to a new CSV file.
- Loads cleaned data into a **SQLite database** using SQLAlchemy.
- Runs example queries inside Python to verify data.

---

## 🗄 Example SQL queries practiced

```sql
-- Find user signups by date
SELECT signup_date, COUNT(*) AS num_users
FROM users
GROUP BY signup_date;

-- Join customers and orders to get total spending
SELECT c.customer_name, SUM(o.amount) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_name;
