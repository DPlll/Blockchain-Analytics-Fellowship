# analysis.py
import sqlite3
import pandas as pd
from Modules.logger_config import configure_logger
from Modules.transaction_graph import TransactionGraphAnalyzer
from Modules.database import ETH_Database  # Ensure you are using your database wrapper

# Set up logger
logger = configure_logger(log_file='logs/crypto_analysis.log')

def analyze_transactions(known_fraud_addresses):
    logger.info(f"{__name__} is running...\n")
    logger.info(f"Beggining Dynamicly Recursive Blochain Analysis.\n")
    fraud_addresses = set(address.lower().strip() for address in known_fraud_addresses)  # Normalize addresses

    # Initialize the database object
    logger.info(f"Accsessing database {ETH_Database}\n")
    eth_db = ETH_Database('database/etherscan_data.db')  # Use the ETH_Database wrapper
    conn = eth_db.conn  # Access the connection object directly

    # Load data into DataFrame
    df = pd.read_sql_query("SELECT * FROM transactions", conn)
    logger.info(f"--- SQL DB Data SUMMARY ---")
    print(df)  # Debugging: Print the DataFrame to check loaded data

    # Check for fraud wallets missing in the DataFrame
    missing_in_data = [
        wallet for wallet in known_fraud_addresses
        if wallet not in df['tx_from'].values and wallet not in df['tx_to'].values
    ]
    if missing_in_data:
        logger.info(f"Fraud wallets missing in the DataFrame: {len(missing_in_data)}")
    else:
        logger.info("All fraud wallets are present in the DataFrame.")

    # Normalize wallet addresses in the DataFrame
    df['tx_from'] = df['tx_from'].str.lower().str.strip()
    df['tx_to'] = df['tx_to'].str.lower().str.strip()

    # Initialize graph analyzer
    graph_analyzer = TransactionGraphAnalyzer(df, eth_db)

    # Debugging: Check if fraud wallets are in the graph
    missing_in_graph = [wallet for wallet in fraud_addresses if wallet not in graph_analyzer.graph]
    if missing_in_graph:
        logger.info(f"Fraud wallets missing in graph: {missing_in_graph}")
    else:
        logger.info("All fraud wallets are present in the graph.")

    # Analyze patterns starting from each known fraud address
    results = {}
    for start_address in fraud_addresses:
        logger.info(f"Analyzing transaction patterns from {start_address}")
        analysis = graph_analyzer.analyze_fraud_patterns(start_address, fraud_addresses)
        results[start_address] = analysis

        # Log findings
        logger.info(f"\n ---  Dynamic Search Analysis Summary  --- \n")
        logger.info(f"{__name__} Found {analysis['summary']['total_fraud_wallets_reached']} connected fraud wallets")
        logger.info(f"{__name__} Discovered {analysis['summary']['unique_paths_found']['bfs']} unique paths using BFS")
        logger.info(f"{__name__} Discovered {analysis['summary']['unique_paths_found']['dfs']} unique paths using DFS")

    # Close the connection to the SQLite database
    eth_db.close()  # Use the wrapper's close method
    return results





