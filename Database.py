import sqlite3

# Connect to the SQLite database (creates the database file if it doesn't exist)
conn = sqlite3.connect('etherscan_data.db')  # File-based database, 'etherscan_data.db' is the file name.
cursor = conn.cursor()

# Create a table for storing Ethereum transactions
cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        hash TEXT PRIMARY KEY,  -- Unique transaction hash (identifier)
        from_address TEXT,       -- Address that sent the ETH
        to_address TEXT,         -- Address that received the ETH
        value_eth REAL,          -- Transaction value in ETH
        block_number INTEGER,    -- Block number the transaction was included in
        timestamp TEXT           -- Unix timestamp of the transaction
    )
''')

# Commit the changes to the database and close the connection
conn.commit()
conn.close()
