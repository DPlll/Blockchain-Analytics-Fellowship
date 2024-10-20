# A separate program to trace Bitcoin transactions recursively using Blockchain.info API
import requests

BASE_URL = "https://blockchain.info"

# Function to get transaction details by transaction hash
def get_transaction(tx_hash):
    url = f"{BASE_URL}/rawtx/{tx_hash}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching transactions for {tx_hash}")
        return None

# Function to get block details by block hash
def get_block(block_hash):
    url = f"{BASE_URL}/rawblock/{block_hash}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching block {block_hash}")
        return None

# Recursive function to track Bitcoin's UTXO chain
def track_bitcoin(identifier, is_block=False, depth=0, max_depth=5):
    # Set a restriction on recursive traceback (Check if the maximum depth has been reached)
    if depth > max_depth:
        print(f"Max depth of {max_depth} reached. Stopping recursion.")
        return

    # Check if the identifier is a block or transaction
    if is_block:
        block_data = get_block(identifier)
        if not block_data:
            print(f"Error: Block {identifier} not found")
            return
        # Iterate over transactions in the block
        for tx_hash in block_data.get('tx', []):
            track_bitcoin(tx_hash, is_block=False, depth=depth+1, max_depth=max_depth)
    # If the identifier is a transaction, get the transaction details
    else:
        tx_data = get_transaction(identifier)
        if not tx_data:
            print(f"Recursive UTXO tracking error. Transaction {identifier} not found")
            return
        
        # Print transaction info
        print(f"Transaction Hash: {identifier}:")
        for input_data in tx_data.get('inputs', []):
            prev_tx_hash = input_data.get('prev_out', {}).get('tx_index')
            print(f"  Input from transaction {prev_tx_hash} - Value: {input_data.get('prev_out', {}).get('value')} satoshis")
        
        for output_data in tx_data.get('out', []):
            print(f"  Output to address {output_data.get('addr')} - Value: {output_data.get('value')} satoshis")

        # Continue tracking if there are inputs (previous transactions)
        for input_data in tx_data.get('inputs', []):
            if 'prev_out' in input_data:
                prev_tx_hash = input_data['prev_out']['tx_index']
                if prev_tx_hash:
                    track_bitcoin(prev_tx_hash, is_block=False, depth=depth+1, max_depth=max_depth)

# Example usage: Start tracking UTXO's recursivley from a known block hash or transaction hash
identifier = '03fd119f26ea45ca83bbd0aef9cc38df027b72eb8d7c1d1f7c44874cc575c5fd'  # Replace with actual block hash or transaction hash (blockchain.com for most recent hashes)
is_block = False  # Set to True if the identifier is a block hash, False if it's a transaction hash
max_depth = 5  # Set the maximum depth for recursion
track_bitcoin(identifier, is_block, max_depth=max_depth)
