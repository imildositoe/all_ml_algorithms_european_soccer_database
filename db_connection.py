import sqlite3
import pandas as pd

# Connect to the sqlite db
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

country = cursor.execute('SELECT * FROM Country')
df_country = pd.DataFrame(country)
