# 9/11/24 Main Page that will call other code spaces
#Built on Python v3.12.2


#Imports 
import os
import requests
import sqlite3 
from datetime import datetime
from dotenv import load_dotenv 
from database import ETH_Database


#Load environment variables from .env file 
load_dotenv()

# Set wallet adress variable 
address = '0x4838B106FCe9647Bdf1E7877BF73cE8B0BAD5f97'

# Assign environment variables to constant variuables/ Initialize DB
ETH_API_KEY = (os.getenv('ETH_API_KEY'))
ETH_DB = ETH_Database()

# connect to the etherscan api
url = "https://api.etherscan.io/api"


########################################
# Parameters for the BALANCE API request#
#########################################
params = {
    'module': 'account',
    'action': 'balance',
    'address': address,
    'tag': 'latest',
    'apikey': ETH_API_KEY
}

# Send request to the API
response = requests.get(url, params=params)

# Parse the response as JSON
data = response.json()

# Get the balance from the response (balance is returned in Wei)
balance_wei = data['result']
balance_eth = int(balance_wei) / 10**18  # Convert Wei to ETH

print(f'Balance of address {address}: {balance_eth} ETH')


#############################################################
# --- Get a list of 'Normal' Transactions for the Address ---
#############################################################
# Parameters for the normal transactions API request
txlist_params = {
    'module': 'account',
    'action': 'txlist',
    'address': address,
    'startblock': 0,  # You can change this to limit the blocks
    'endblock': 99999999,  # To include all blocks up to the latest
    'sort': 'asc',  # You can also use 'desc' to sort by newest first
    'apikey': ETH_API_KEY
}

# Send request to get normal transactions
txlist_response = requests.get(url, params=txlist_params)
# Parse the transaction list response as JSON
txlist_data = txlist_response.json()

# Check if the result is not empty
if 'result' in txlist_data:
    transactions = txlist_data['result']

    print(f"\nNormal transactions for address ({address}):")

    # Loop through the list of transactions and print details
    for tx in transactions:
        tx_hash = tx['hash']
        tx_from = tx['from']
        tx_to = tx['to']
        tx_value = int(tx['value']) / 10**18  # Convert from Wei to ETH
        tx_block = tx['blockNumber']
        tx_time = tx['timeStamp']

        # ---- Initialize the database with the unique filename ----
        ETH_DB = ETH_Database(db_name='etherscan_data.db')
        

        # Insert each transaction into the database
        ETH_DB.insert_transaction(tx_hash, tx_from, tx_to, tx_value, tx_block, tx_time)

        #print(f"\nTransaction Hash: {tx_hash}")
        #print(f"From: {tx_from}")
        #print(f"To: {tx_to}")
        #print(f"Value: {tx_value} ETH")
        #print(f"Block Number: {tx_block}")
        #print(f"Timestamp: {tx_time}")

    # Fetch and print all transactions from the database (optional)
    results = ETH_DB.fetch_all_transactions()

    count_rows = len(results)
    print("\nStored transactions in the database:")
    print(f"\nTotal of {count_rows} transactions stored")
    


    # Close the database connection
    ETH_DB.close()
    

else:
    print("No transactions found for this address.")

# --- Get balance of multiple addresses (optional, you can expand here later) ---
