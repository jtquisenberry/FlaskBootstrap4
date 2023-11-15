import os
import sqlite3

if not os.path.exists('address.db'):
    conn = sqlite3.connect('address.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE address
                 (name text, number text, street text, state text, zip text)''')
    conn.commit()
    conn.close()
