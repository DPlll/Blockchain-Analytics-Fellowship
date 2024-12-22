import os
import sys
from Modules.main_util import fetch_multi_balances, fetch_balance, fetch_and_store_transactions
from Modules.logger_config import configure_logger

# Set up logger to output to both a file and the terminal with colors
logger = configure_logger(log_file='logs/crypto_analysis.log')

# Set wallet address for API
address = os.getenv('address')
addresses = os.getenv('addresses')
print(f'address: {address}')
print(f'addresses: {addresses}')

def main():
    logger.info(f"{__name__} is running...")

    # Fetch and log multi balances
    fetch_multi_balances(addresses)
    
    # Fetch and log single balance
#    fetch_balance(address)
    
    # Fetch and store transactions
    fetch_and_store_transactions(address)

    logger.info(f"{__name__} is done. Check logs/crypto_analysis.log for more details and database/etherscan_data.db for transactions details pulled from the blockchain.")

if __name__ == "__main__":
    main()
