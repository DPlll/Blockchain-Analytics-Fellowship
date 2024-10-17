#Blockcahin Analytics Fellowship class creation 
# 9/18/24 New Modular Main Page that will call other modules
#Built on Python v3.12.2 

# Imports
import os
import sys
from Modules.api_module import get_balance, get_transactions, get_balances
from Modules.database import ETH_Database
from Modules.logger_config import configure_logger

# Set up logger to output to both a file and the terminal with colors
logger = configure_logger(log_file='logs/crypto_analysis.log')

# Set wallet address for API
address = os.getenv('address')
addresses= os.getenv('addresses')
print(f'address: {address}')
print(f'addresses: {addresses}')

# Initialize the database with the unique filename
ETH_DB = ETH_Database(db_name='database/etherscan_data.db')

def main():
    logger.info(f"{__name__} is running...")
    
    # --- Call get multi balance from the API module and print balance ---
    balances = get_balances(addresses)
    if balances: # Check if balances is not None or empty
        for balance_info in balances:
            maddress = balance_info['address']
            mbalance = balance_info['balance']
            logger.info(f" Multi Balance of address {maddress} : {mbalance} ETH")
        else:
            logger.warning("No balances for multibalance were retrieved or addresses are invalid.")
    # --- Call get_balance from api module and print balance ---
    balance = get_balance(address)
    logger.info(f"Balance of address {address}: {balance} ETH") 

    # --- Call get_transactions from the API module and store the transactions in the database ---
    transactions = get_transactions(address)
    logger.info(f"Retreiving transactions for {address} from etherscan...") #print address
    if transactions:
        logger.info(f"Retreived {len(transactions)} Transactions from {address} via Etherscan...") #count transaction and print total
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
        logger.warning(f" {__name__} No transactional data received for {address} from etherscan.")

    logger.info(f"{__name__} has completed successfully.")



# call main
if __name__ == "__main__":
    main()