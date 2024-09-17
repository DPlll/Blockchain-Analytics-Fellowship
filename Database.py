import sqlite3


# Connect to the SQLite database (creates the database file if it doesn't exist)
conn = sqlite3.connect('etherscan_data.db')  # File-based database, 'etherscan_data.db' is the file name
cursor = conn.cursor()

#Initalize Class 
class ETH_Database:
    def __init__(self, db_name='etherscan_data.db'):
        # Initialize the connection to the SQLite database
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()  # Create the table when the class is initialized


    def create_table(self):
        # Create a table for storing Ethereum transactions , set name "transactions" and create colums "Hash, From, to ..." with set data types "PRIMARY KEY, TEXT..." 
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                hash TEXT PRIMARY KEY,  -- Unique transaction hash (identifier) 
                from_address TEXT,       -- Address that sent the ETH
                to_address TEXT,         -- Address that received the ETH
                value_eth REAL,          -- Transaction value in ETH
                block_number INTEGER,    -- Block number the transaction was included in
                timestamp INTEGER           -- Unix timestamp of the transaction
            )
        ''')
        self.conn.commit() 


    def insert_transaction(self, tx_hash, tx_from, tx_to, tx_value, tx_block, tx_time):
        # Insert a transaction into the database
        self.cursor.execute('''
            INSERT OR IGNORE INTO transactions (hash, from_address, to_address, value_eth, block_number, timestamp)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (tx_hash, tx_from, tx_to, tx_value, tx_block, tx_time))
        self.conn.commit()

    def fetch_all_transactions(self):
        # Fetch all transactions from the database
        self.cursor.execute("SELECT * FROM transactions")
        return self.cursor.fetchall()
    
    def clear_table(self):
        # Clear all data from the transactions table
        self.cursor.execute("DELETE FROM transactions")
        self.conn.commit()

    def close(self):
        # Close the database connection
        self.conn.close()