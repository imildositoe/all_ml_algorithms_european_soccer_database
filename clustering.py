import pandas as pd
import sqlite3

conn = sqlite3.connect('database.sqlite')
df_pp_attributes = pd.read_sql('SELECT * FROM Player p JOIN Player_Attributes pa ON p.player_api_id = pa.player_api_id', conn)
conn.close()

print(df_pp_attributes)