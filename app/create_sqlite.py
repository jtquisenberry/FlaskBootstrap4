import sqlite3

# Create a new database file
conn = sqlite3.connect('database.db')

# Create a new table named Product
conn.execute('''CREATE TABLE Product
             (Name TEXT NOT NULL,
             Color TEXT NOT NULL,
             Quantity INT NOT NULL);''')

# Save the changes
conn.commit()

# Close the connection
conn.close()
