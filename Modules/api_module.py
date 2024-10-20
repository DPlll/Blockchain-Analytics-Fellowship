# Module for all API calls and interactions
#9/18/2024

#load imports
import requests
import os
from dotenv import load_dotenv
from Modules.logger_config import configure_logger

#Load environment variables from .env file 
load_dotenv()

# Assign environment variables to constant variuables
ETH_API_KEY = os.getenv('ETH_API_KEY')

# Set up logger
logger = configure_logger(log_file='logs/crypto_analysis.log')

# Set the root API URL for etherscan
url = "https://api.etherscan.io/api"

# --- Etherscan- Get balance for a single address function ---
def get_balance(address):
    params = {
        'module': 'account',
        'action': 'balance',
        'address': address, #address needing to be tracked
        'tag': 'latest',
        'apikey': ETH_API_KEY
    }
    response = requests.get(url, params=params) # get responce/ send inqury 
    data = response.json() # Parse json request to python 
    balance_wei = data['result']
    balance_eth = int(balance_wei) / 10**18  # Convert Wei to ETH
    return balance_eth,

# --- Etherscan- Get list of 'Normal' transactions for a single address (up to a maximum of 10,000 records only)---
def get_transactions(address, startblock=0, endblock=99999999, sort='desc'):
    params = {
        'module': 'account', 
        'action': 'txlist',
        'address': address, #address needing to be tracked
        'startblock': startblock, # You can change this to limit the blocks
        'endblock': endblock, #To include all blocks up to the latest
        'sort': sort,  # Can use 'asc' for oldest first or use 'desc' to sort by newest first
        'apikey': ETH_API_KEY
    }
    # Send request to get normal transactions
    response = requests.get(url, params=params)
    data = response.json()  # Parse the transaction list response as JSON
    if 'result' in data:
        return data['result']  # Return list of transactions
    else:
        logger.error("(m.api)Normal Transactions: Error, received empty list from etherscan")
        return []  # Return empty list if no transactions are found or error occurs
    
# --- Etherscan- Get Multi Balance for multi adresses in a single call (up to 20 addresses) --- 
def get_balances(addresses):
    params = {
        'module': 'account',
        'action': 'balancemulti',
        'address': addresses,
        'tag': 'latest',
        'apikey': ETH_API_KEY
    }
    response = requests.get(url, params=params) # get responce/ send inqury 
    data = response.json() # Parse json request to python 
    #handle the response from the Etherscan API else log error
    if 'result' in data:
        balance_list = [] # Create an empty list to store the address and balance
        # Loop through each result to convert balances from wei to ETH
        for item in data['result']:
            balance_wei = int(item['balance'])
            balance_eth = balance_wei / 10**18  # Convert Wei to ETH
            
            # Append address and balance to the balances_list (fix here)
            balance_list.append({
                'address': item['account'],
                'balance': balance_eth
            })
        return balance_list
    else:
        logger.error(f"MultiBalance: API returned empty result: {data}")
        return None
