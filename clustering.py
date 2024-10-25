import pandas as pd
import sqlite3

df_player = []
df_player_attributes = []

def get_player():
    global df_player
    conn = sqlite3.connect('database.sqlite')
    cursor = conn.cursor()
    player = cursor.execute('SELECT * FROM Player')
    df_player = pd.DataFrame(player)
    conn.close()

def get_player_attributes():
    global df_player_attributes
    conn = sqlite3.connect('database.sqlite')
    cursor = conn.cursor()
    player_attributes = cursor.execute('SELECT * FROM Player_Attributes')
    df_player_attributes = pd.DataFrame(player_attributes)
    conn.close()

# print(df_player)
# get_player_attributes()
print(df_player_attributes)