# analysis.py
import sqlite3
import pandas as pd
from logger_config import configure_logger
from transaction_graph import TransactionGraphAnalyzer

# Set up logger
logger = configure_logger(log_file='logs/crypto_analysis.log')

# Analyze transactions for fraud patterns using graph traversal. Args: known_fraud_addresses: List of known fraudulent wallet addresses
def analyze_transactions(known_fraud_addresses):

    # Connect to the database
    conn = sqlite3.connect('database/etherscan_data.db')
    
    # Load data into DataFrame
    df = pd.read_sql_query("SELECT * FROM transactions", conn)
    conn.close()
    
    # Initialize graph analyzer
    graph_analyzer = TransactionGraphAnalyzer(df)
    
    # Convert addresses to set for faster lookup
    fraud_addresses = set(known_fraud_addresses)
    
    # Analyze patterns starting from each known fraud address
    results = {}
    for start_address in fraud_addresses:
        logger.info(f"Analyzing transaction patterns from {start_address}")
        analysis = graph_analyzer.analyze_fraud_patterns(start_address, fraud_addresses)
        results[start_address] = analysis
        
        # Log findings
        logger.info(f"Found {analysis['summary']['total_fraud_wallets_reached']} connected fraud wallets")
        logger.info(f"Discovered {analysis['summary']['unique_paths_found']['bfs']} unique paths using BFS")
        logger.info(f"Discovered {analysis['summary']['unique_paths_found']['dfs']} unique paths using DFS")
    
    return results

# Example usage:
if __name__ == "__main__":
    # Use the fraud addresses from your algo_math_model.txt
    known_fraud_addresses = [
        '0x3130A00D2F482c35F32044Ace12c64C1dB423cf9', # v1 (root node/address)
        '0xf3A78579431F4C9C31d3E4180D4783213787d861', # v2 
        '0xE868d4bCDA51DcCe5269d74eDaa65162a2c04e66', # v3
        '0x32f0591087CFC166B6CFCef97dB845Fb27A1274B', # v4
        '0x463676ac589C4D70b158Bda0F2b03C1A3260e829', # v5
        '0x4AB17933dE56f049Ca81ae2913608e14ca7319Bd', # v6
        '0x4AB17933dE56f049Ca81ae2913608e14ca7319Bd', # v7
        '0xfF59d11d5F0D448AD84E246aC2c04F6678e85673', # v8
        '0x24F6Caa8E722fA7AC9509C6218a5482195f7C5eE', # v9 (cold storage, no outgoing transactions)
        '0x981D5DD367b022a162c223cB59B50e1B167098a0' # v10 (cold storage, no outgoing transactions)
    ]

    
    results = analyze_transactions(known_fraud_addresses)
    
    # Display detailed analysis
    for start_address, analysis in results.items():
        print(f"\nAnalysis starting from {start_address}:")
        print("BFS Paths found:")
        for end_addr, paths in analysis['bfs_paths'].items():
            print(f"  To {end_addr}: {len(paths)} paths found")
        print("DFS Paths found:")
        for end_addr, paths in analysis['dfs_paths'].items():
            print(f"  To {end_addr}: {len(paths)} paths found")




