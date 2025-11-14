import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect("ecom.db")

# Load the SQL query from file
with open("queries/customer_orders.sql", "r") as file:
    query = file.read()

# Run the query and load results into a DataFrame
df = pd.read_sql_query(query, conn)

# Display the first few rows
print(df.head())

# Close the connection
conn.close()