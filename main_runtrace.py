from Modules.analysis import analyze_transactions

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

    # Call the function
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
