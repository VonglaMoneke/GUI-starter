import sqlite3

global user
user = ' ' + 'Tedward'
global conn
global c

conn = sqlite3.connect('tester.db')
c = conn.cursor()
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS'+ str(user)+'(Username TEXT, Password TEXT)')
create_table()
