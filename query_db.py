import sqlite3

# Connect to SQLite Database
conn = sqlite3.connect('solar.db')
print("Connected to solar.db database.")

# Simple GROUP BY Query
for row in conn.execute("SELECT Year, COUNT(*) FROM solar_ops GROUP BY Year"):
	print(row)

# Close the Connection
conn.close()
print("Query complete, connection closed.")