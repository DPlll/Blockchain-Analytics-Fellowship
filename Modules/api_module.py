# Module for all API calls and interactions
#9/18/2024

#load imports
import requests
import os
from dotenv import load_dotenv
from Modules.logger_config import configure_logger

#Load environment variables from .env file 
load_dotenv()

# Assign environment variables to constant variuables/ Initialize DB
ETH_API_KEY = os.getenv('ETH_API_KEY')

# Set up logger
logger = configure_logger(log_file='logs/crypto_analysis.log')

# connect to the etherscan api
url = "https://api.etherscan.io/api"

# --- Etherscan- Get balance for a adress function ---
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
    return balance_eth

# --- Etherscan- Get list of 'Normal' transactions for a adress ---
def get_transactions(address, startblock=0, endblock=99999999, sort='asc'):
    params = {
        'module': 'account',
        'action': 'txlist',
        'address': address, #address needing to be tracked
        'startblock': startblock, # You can change this to limit the blocks
        'endblock': endblock, #To include all blocks up to the latest
        'sort': sort,  # Can use 'asc' for loldest first or use 'desc' to sort by newest first
        'apikey': ETH_API_KEY
    }
    # Send request to get normal transactions
    response = requests.get(url, params=params)
    # Parse the transaction list response as JSON
    data = response.json()
    if 'result' in data:
        return data['result']  # Return list of transactions
    else:
        return print("Normal Transactions: Error, received empty list from etherscan")  # Return empty list if no transactions are found

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
    if 'result' in data:
        # Loop through each result to convert balances from wei to ETH
        balance_list = []
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