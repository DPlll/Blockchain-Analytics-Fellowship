#Blockcahin Analytics Fellowship class creation 
# 9/18/24 New Modular Main Page that will call other modules
#Built on Python v3.12.2 

# Imports
import os
from modules.api_module import get_balance, get_transactions
from modules.database import ETH_Database
from modules.logger_config import configure_logger

# Set up logger
logger = configure_logger(log_folder='logs', log_file='crypto_analysis.log')

# Set wallet address for API
address = os.getenv('address')

# Initialize the database with the unique filename
ETH_DB = ETH_Database(db_name='etherscan_data.db')

def main():
    logger.info(f"{__name__} is running...")
    # Call get balance from the API module and print balance
    balance = get_balance(address)
    logger.info(f"Balance of address {address}: {balance} ETH")
    # Get the transaction list and store it in the database
    transactions = get_transactions(address)
    logger.info(f"Retreiving Transactions from Etherscan.")
    if transactions:
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
        logger.info(f"Stored transactions in the database: {count_rows}")

        # Close the database connection
        ETH_DB.close()
    else:
        logger.warning(f"No transactions found for {address}.")

# call main
if __name__ == "__main__":
    main()