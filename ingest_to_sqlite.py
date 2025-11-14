import pandas as pd
import sqlite3

# Connect to SQLite database (creates ecom.db if it doesn't exist)
conn = sqlite3.connect("ecom.db")

# Load CSVs from the current folder
customers = pd.read_csv("generate_customers.csv")
products = pd.read_csv("generate_products.csv")
orders = pd.read_csv("generate_orders.csv")
reviews = pd.read_csv("generate_reviews.csv")
inventory = pd.read_csv("generate_inventory.csv")

# Write to SQLite tables
customers.to_sql("customers", conn, if_exists="replace", index=False)
products.to_sql("products", conn, if_exists="replace", index=False)
orders.to_sql("orders", conn, if_exists="replace", index=False)
reviews.to_sql("reviews", conn, if_exists="replace", index=False)
inventory.to_sql("inventory", conn, if_exists="replace", index=False)

conn.commit()
conn.close()

print("✅ All CSV files ingested into ecom.db successfully!")