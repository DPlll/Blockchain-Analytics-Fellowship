# Crypto-Analytics-Forensics 

Create a code base and roadmap on how to track blockchain transactions for a possible future class on crypto analytics and forensics 

Student Goals: Create a crypto tracking application project and roadmap for the potential future
course and be able to get kinks out of the way for future students.

Student Tasks: Reasearch, to figure out how if possible to track bitcoin using a private self
created code base utilizing some basic cryto api’s and other tools.

Specific Expectations: Figure out whether this is a probable course for students to take and if it is
possible. If possible, create a code base that can track bitcoin transactions and create a road map
(list of useful skills student will need) inorder to complete the course if chosen to be a viable
course.
#####################################################################################################
# ---- ROAD MAP ---- #
Phase 1: Setup and Infrastructure
Understand Ethereum & Etherscan API

Study Ethereum’s wallet architecture and how transactions work on the blockchain.
Familiarize yourself with the Etherscan API, focusing on the getTransactionByHash and getTransactionsByAddress methods for tracking wallet activity.
Set Up ETH Wallets

Create 5 to 10 Ethereum wallets using a wallet tool like MetaMask, MyEtherWallet, or programmatically with a library such as eth-account in Python.
Fund each wallet with test ETH from a testnet like Rinkeby or Goerli (since this is a closed network, using a testnet avoids real costs).
Configure an Etherscan Account

Register for an Etherscan API key to access the Ethereum blockchain data.
Review the rate limits and decide whether the free tier is sufficient for your needs or if you require a paid plan.
Phase 2: Develop Core Functionality
Create Python Environment

Set up a Python environment with necessary dependencies, such as web3.py for blockchain interaction and requests for API calls.
Install libraries: web3, etherscan-python, and dotenv (to manage API keys securely).
Generate Wallet Transactions

Write scripts that send ETH between the wallets programmatically. You can use web3.py to create, sign, and broadcast transactions between the wallets.
For testing, create a loop to simulate multiple transactions in various directions between the wallets.
Track Transactions with Etherscan

Use Etherscan’s API to track incoming and outgoing transactions for each wallet.
Focus on tracking data like from, to, value, timestamp, and transaction hash.
Store and Organize Transaction Data

Design a data structure (using Python dictionaries, Pandas DataFrame, or an SQLite database) to store transaction details for each wallet.
Ensure each transaction is linked to the corresponding sender and receiver in your closed network.

Phase 3: Reporting and Visualization
Build Transaction Reporting Tool

Write functions that summarize the transaction activity for each wallet, such as total ETH sent, total ETH received, and transaction history.
Consider implementing a real-time tracker that fetches and updates transaction data periodically (e.g., every minute).
Create a Dashboard (Optional)

If you want a visual representation, you can create a basic dashboard using Python libraries like Dash, Streamlit, or Plotly to visualize wallet balances and transaction flows.
Alternatively, you can use a frontend framework like React to build a more advanced interface.

Phase 4: Testing and Deployment
Test on Ethereum Testnets

Thoroughly test the system on the Rinkeby or Goerli testnet, simulating various transaction volumes.
Debug any errors related to API requests, transaction confirmations, or wallet interactions.
Deploy

Once stable, deploy the codebase in a more permanent environment, such as a cloud server (e.g., AWS or DigitalOcean) if you want continuous tracking.
Ensure proper handling of API rate limits and error handling for failed API requests.
Documentation and Maintenance

Document the codebase, including instructions for setting up wallets, interacting with Etherscan API, and running the tracker.
Consider implementing logging for long-term transaction tracking and debugging.
# ---- WORKFLOW ---- #  
1. Create ENV and gitignore for ethrscan api key 
2. create main.py and import 
3. Create a Get multi adresses balance page and import class into main.py
4. Create a file for Getting a list of 'Normal' Transactions for the Addresses and call in main.py
5. Store and Organize Transaction Data- Design a data structure (using Python dictionaries, Pandas DataFrame, or an SQLite database) to store transaction details for each wallet.
6. Run all the reponse wallet transaction data threw a algo to sort and organize repeated sends and adresses 
7. try to visualize the transactions using a data visualizer like networkx 