# A seperate program to trace Bitcoin transactions recursivley using Blockchain.info API 
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

# --- Recursive function to track Bitcoin's UTXO chain ---
def track_bitcoin(tx_hash):
    tx_data = get_transaction(tx_hash)
    if not tx_data:
        print(f" Recursive UTXO tracking error. Transaction {tx_hash} not found")
        return
    
    # Print transaction info
    print(f"Transaction Hash:{tx_hash}:")
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
                track_bitcoin(prev_tx_hash)

# Example: Start tracking from a known transaction (coinbase transaction)
start_tx = '03fd119f26ea45ca83bbd0aef9cc38df027b72eb8d7c1d1f7c44874cc575c5fd' # Transaction/Hash ID (*random bloackhain.com transaction)
track_bitcoin(start_tx)

