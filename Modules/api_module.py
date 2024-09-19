# Module for all API calls and interactions
#9/18/2024

#load imports
import requests
import os
from dotenv import load_dotenv

#Load environment variables from .env file 
load_dotenv()

# Assign environment variables to constant variuables/ Initialize DB
ETH_API_KEY = os.getenv('ETH_API_KEY')
# connect to the etherscan api
url = "https://api.etherscan.io/api"

# --- Etherscan- Get balance for a adress function ---
def get_balance(address):
    params = {
        'module': 'account',
        'action': 'balance',
        'address': address,
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

# --- Etherscan- Get Balnce for multiple transactions in a single call (up to 20 addresses)
#set adresses for multi balance
#addresses= [
#    '0x9df8c5F47527B6E20D55D03d35C17fc44155c9BC',
#    '0x812Bc129aFC70869DcA342Dd8dFdaa514DC47377',
#    'xb2C657c65A5CeFdc05bFF86DE25017B8d5C11BA3',
#]
#def get_balance(addresses):
#    params = {
#        'module': 'account',
#        'action': 'balancemulti',
#        'address': addresses,
#        'tag': 'latest',
#        'apikey': ETH_API_KEY
#    }
#    response = requests.get(url, params=params) # get responce/ send inqury 
#    data = response.json() # Parse json request to python 
#    balance_wei = data['result']
#    balance_eth = int(balance_wei) / 10**18  # Convert Wei to ETH
#    return balance_eth
