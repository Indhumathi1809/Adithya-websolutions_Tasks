# cross_platform_interaction.py

import sqlite3

# Database setup
conn = sqlite3.connect('interaction_db.sqlite')
cursor = conn.cursor()

# Create a table for storing interactions
cursor.execute('''
    CREATE TABLE IF NOT EXISTS interactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        platform TEXT,
        action TEXT,
        data TEXT
    )
''')
conn.commit()

# Function to log interactions
def log_interaction(platform, action, data):
    cursor.execute('INSERT INTO interactions (platform, action, data) VALUES (?, ?, ?)', (platform, action, data))
    conn.commit()

# Function to retrieve interactions
def get_interactions():
    cursor.execute('SELECT * FROM interactions')
    return cursor.fetchall()

# Example usage
if __name__ == "__main__":
    # Simulate an Android interaction
    log_interaction('Android', 'Button Click', 'Submit Data')

    # Simulate a Windows interaction
    log_interaction('Windows', 'Menu Selection', 'Open File')

    # Retrieve and print all interactions
    interactions = get_interactions()
    print("All Interactions:")
    for interaction in interactions:
        print(interaction)

# Close the database connection
conn.close()
