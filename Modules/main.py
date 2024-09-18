#Blockcahin Analytics Fellowship class creation 
# 9/18/24 New Modular Main Page that will call other modules
#Built on Python v3.12.2 

# Imports
from api_module import get_balance, get_transactions
from database import ETH_Database
from logger_config import configure_logger

# Set up logger
logger = configure_logger()

# Set wallet address for API
address = '0x4838B106FCe9647Bdf1E7877BF73cE8B0BAD5f97'

def main():
    # Call get balance from the API module and print balance
    balance = get_balance(address)
    print(f'Balance of address {address}: {balance} ETH')

    # Get the transaction list and store it in the database
    transactions = get_transactions(address)
    if transactions:
        # Initialize the database with the unique filename
        ETH_DB = ETH_Database(db_name='etherscan_data.db')
        
        print(f"\nNormal transactions for address ({address}):")

        for tx in transactions:
            tx_hash = tx['hash']
            tx_from = tx['from']
            tx_to = tx['to']
            tx_value = int(tx['value']) / 10**18  # Convert from Wei to ETH
            tx_block = tx['blockNumber'] 
            tx_time = tx['timeStamp']

            # Insert each transaction into the database
            ETH_DB.insert_transaction(tx_hash, tx_from, tx_to, tx_value, tx_block, tx_time)

        # Fetch and print all transactions from the database
        results = ETH_DB.fetch_all_transactions()
        #count rows of data imported to sqplite via etherscan api and print total
        count_rows = len(results)
        print(f"\nStored transactions in the database: {count_rows}")

        # Close the database connection
        ETH_DB.close()
    else:
        print("ERROR: No transactions found for this address.")

# call main
if __name__ == "__main__":
    main()