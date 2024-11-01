import logging
from Modules.api_module import get_balance, get_transactions, get_balances
from Modules.database import ETH_Database

# Initialize the database with the unique filename
ETH_DB = ETH_Database(db_name='database/etherscan_data.db')
# Initialize the logger
logger = logging.getLogger(__name__)


# --- Function to get multi balance from the API module and print balance ---
def fetch_multi_balances(addresses):
    balances = get_balances(addresses)
    if balances:  # Check if balances is not None or empty
        for balance_info in balances:
            maddress = balance_info['address']
            mbalance = balance_info['balance']
            logger.info(f"Multi Balance of address {maddress}: {mbalance} ETH")
    else:
        logger.warning("No balances for multibalance were retrieved or addresses are invalid.")

# --- Function to get_balance from api module and print balance ---
def fetch_balance(address):
    balance = get_balance(address)
    logger.info(f"Balance of address {address}: {balance} ETH")
    return balance

# --- Call get_transactions from the API module and store the transactions in the database ---
def fetch_and_store_transactions(address): 
    transactions = get_transactions(address) # Get transactions from the API
    logger.info(f"Retrieving transactions for {address} from etherscan...")  # print address
    if transactions:  # Check if transactions is not None or empty
        logger.info(f"Retrieved {len(transactions)} Transactions from {address} via Etherscan...")  # count transaction and print total
        for tx in transactions:
            tx_hash = tx['hash']
            tx_from = tx['from']
            tx_to = tx['to']
            tx_value = int(tx['value']) / 10**18  # Convert from Wei to ETH
            tx_block = tx['blockNumber']
            tx_time = tx['timeStamp']
            # Insert each transaction into the database
            ETH_DB.insert_transaction(tx_hash, tx_from, tx_to, tx_value, tx_block, tx_time)
            
        results = ETH_DB.fetch_all_transactions() # Fetch and print all transactions from the database
        count_rows = len(results) #count rows of data imported to sqplite via etherscan api and print total
        logger.info(f"Stored transactions in the database: {count_rows}")
        logger.info('Closing the database connection...')
        ETH_DB.close() # Close the database connection
    else:
        logger.warning(f" {__name__} No transactional data received for {address} from etherscan.")

    logger.info(f"{__name__} has completed successfully.")
