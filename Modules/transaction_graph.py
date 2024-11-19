# transaction_graph.py
import pandas as pd
from collections import defaultdict, deque
from typing import Dict, List, Set

class TransactionGraphAnalyzer:
    def __init__(self, transactions_df: pd.DataFrame):
        """
        Initialize the graph analyzer with a DataFrame of transactions.
        
        Args:
            transactions_df: DataFrame with columns 'tx_from', 'tx_to', 'tx_value', 'tx_time'
        """
        self.transactions_df = transactions_df
        self.graph = self._build_graph()
        
    def _build_graph(self) -> Dict[str, List[tuple]]:
        """
        Build an adjacency list representation of the transaction graph.
        Returns a dictionary where keys are wallet addresses and values are lists of
        (destination_address, value, timestamp) tuples.
        """
        graph = defaultdict(list)
        for _, tx in self.transactions_df.iterrows():
            graph[tx['tx_from']].append((tx['tx_to'], tx['tx_value'], tx['tx_time']))
        return graph
    
    def bfs_trace(self, start_address: str, known_fraud_addresses: Set[str]) -> Dict[str, List[tuple]]:
        """
        Perform BFS to trace transactions between known fraud wallets.
        Returns paths of transactions between fraud wallets.
        
        Args:
            start_address: The root fraud wallet address to start from
            known_fraud_addresses: Set of known fraudulent wallet addresses
        """
        queue = deque([(start_address, [(start_address, 0, 0)])])
        visited = set()
        fraud_paths = defaultdict(list)
        
        while queue:
            current_address, path = queue.popleft()
            if current_address in visited:
                continue
                
            visited.add(current_address)
            
            # If we've found a path to another fraud wallet, save it
            if current_address in known_fraud_addresses and current_address != start_address:
                fraud_paths[current_address].append(path)
            
            # Add all neighboring transactions to queue
            for next_addr, value, timestamp in self.graph.get(current_address, []):
                if next_addr not in visited:
                    new_path = path + [(next_addr, value, timestamp)]
                    queue.append((next_addr, new_path))
        
        return fraud_paths
    
    def dfs_trace(self, start_address: str, known_fraud_addresses: Set[str]) -> Dict[str, List[tuple]]:
        """
        Perform DFS to trace transactions between known fraud wallets.
        Returns paths of transactions between fraud wallets.
        
        Args:
            start_address: The root fraud wallet address to start from
            known_fraud_addresses: Set of known fraudulent wallet addresses
        """
        visited = set()
        fraud_paths = defaultdict(list)
        
        def dfs(current_address: str, path: List[tuple]):
            if current_address in visited:
                return
                
            visited.add(current_address)
            
            # If we've found a path to another fraud wallet, save it
            if current_address in known_fraud_addresses and current_address != start_address:
                fraud_paths[current_address].append(path)
            
            # Explore all neighboring transactions
            for next_addr, value, timestamp in self.graph.get(current_address, []):
                if next_addr not in visited:
                    new_path = path + [(next_addr, value, timestamp)]
                    dfs(next_addr, new_path)
        
        # Start DFS from the root fraud wallet
        dfs(start_address, [(start_address, 0, 0)])
        return fraud_paths
    
    def analyze_fraud_patterns(self, start_address: str, known_fraud_addresses: Set[str]) -> dict:
        """
        Analyze transaction patterns using both BFS and DFS.
        Returns a comprehensive analysis of transaction paths and patterns.
        """
        bfs_results = self.bfs_trace(start_address, known_fraud_addresses)
        dfs_results = self.dfs_trace(start_address, known_fraud_addresses)
        
        analysis = {
            'bfs_paths': bfs_results,
            'dfs_paths': dfs_results,
            'summary': {
                'total_fraud_wallets_reached': len(set(bfs_results.keys()) | set(dfs_results.keys())),
                'unique_paths_found': {
                    'bfs': sum(len(paths) for paths in bfs_results.values()),
                    'dfs': sum(len(paths) for paths in dfs_results.values())
                }
            }
        }
        
        return analysis