# This module sets up and deals with the sqlite3 database for storing Ethereum transactions.
import sqlite3

#Initalize Class
class ETH_Database:
    #Initialize connectrion to the SQLite database (creates the database file if it doesn't exist)
    def __init__(self, db_name='database/etherscan_data.db'): # File-based database, 'etherscan_data.db' is the file namet
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table() # Create the table when the class is initialized

# Create a table for storing Ethereum transactions , set name "transactions" and create colums "Hash, From, to ..." with set data types "PRIMARY KEY, TEXT..." 
    def create_table(self):
        """
        Create a table for storing Ethereum transactions if it doesn't exist.
        """
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                tx_hash TEXT,
                                tx_from TEXT,
                                tx_to TEXT,
                                tx_value REAL,
                                tx_block INTEGER,
                                tx_time INTEGER
                            )''')
        self.conn.commit()

    #Inserting transacions
    def insert_transaction(self, tx_hash, tx_from, tx_to, tx_value, tx_block, tx_time):
        """
        Insert a new transaction into the database.
        """
        self.cursor.execute('''INSERT INTO transactions 
                               (tx_hash, tx_from, tx_to, tx_value, tx_block, tx_time) 
                               VALUES (?, ?, ?, ?, ?, ?)''', 
                            (tx_hash, tx_from, tx_to, tx_value, tx_block, tx_time))
        self.conn.commit()

    #Fetch the transactions
    def fetch_all_transactions(self):
        """
        Fetch all transactions from the database.
        """
        self.cursor.execute('SELECT * FROM transactions')
        return self.cursor.fetchall()

    #Clear all the transactions 
    def clear_transactions(self):
        """
        Clear all transactions from the database.
        """
        self.cursor.execute('DELETE FROM transactions')
        self.conn.commit()

    #Close the connection to sqlite database
    def close(self):
        """
        Close the database connection.
        """
        self.conn.close()
