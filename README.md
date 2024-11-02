
<h1 align="center"><strong>Blockchain Analytics</strong></h1>


![logo](assets/blockchainanalyticslogo.png)




<p align="center">
Welcome to the Blockchain Analytics project by DPIII for a potential UMass Lowell course. This tool aims to help users track and analyze fraudulent blockchain transactions, providing insights into cryptocurrency movements and forensics. This README outlines the project plan, including objectives, implementation strategies, development steps, and progress.
</p>

<hr style="height:1px;border-width:1;color:white;background-color:grey;width:90%;margin: 20px auto;">
<p align="center">
  <b>Dependencies:</p>
<p align="center">
  <a href="https://www.python.org/downloads/release/python-3122/" target="_blank">
    <img src="https://img.shields.io/badge/python-v3.12.2-blue?labelColor=gray" alt="python" /></a>
  <a href="https://www.sqlite.org/" target="_blank">
    <img src="https://img.shields.io/badge/sqlite3-003B57?logo=sqlite&logoColor=ffffff" alt="sqlite3" /></a>
  <a href="https://numpy.org/" target="_blank">
    <img src="https://img.shields.io/badge/numpy-777BB4?logo=numpy&logoColor=ffffff" alt="numpy" /></a>
  <a href="https://pandas.pydata.org/" target="_blank">
    <img src="https://img.shields.io/badge/pandas-2C2D72?logo=pandas&logoColor=ffffff" alt="pandas" /></a>
</p>

<hr style="height:1px;border-width:1;color:white;background-color:grey;width:90%;margin: 20px auto;">

# Table of Contents

1. [Project Overview](#project-overview)
   - [Project Objectives](#project-objectives)
   - [Student Goals](#student-goals)
   - [Student Tasks](#student-tasks)
   - [Specific Expectations](#specific-expectations)
2. [Roadmap](#roadmap)
   - [Phase 1: Environment Setup](#phase-1-environment-setup-✓)
   - [Phase 2: Basic Functionality](#phase-2-basic-functionality-✓)
   - [Phase 3: Transaction Tracking](#phase-3-transaction-tracking-✓)
   - [Phase 4: Data Storage and Organization](#phase-4-data-storage-and-organization)
   - [Phase 5: Algorithmic Analysis and Data Visualization](#phase-5-algorithmic-analysis-and-data-visualization)
   - [Phase 6: Documentation and Course Development](#phase-6-documentation-and-course-development)
3. [Workflow](#workflow)
4. [Learning Pathway for Students](#learning-pathway-for-students)
5. [Crypto Analytics Course Outline](#crypto-analytics-course-outline-v1)
   - [Module 1: Python Basics for Crypto Analytics (Part 1)](#module-1-python-basics-for-crypto-analytics-part-1)
   - [Module 2: Python Basics for Crypto Analytics (Part 2)](#module-2-python-basics-for-crypto-analytics-part-2-virtual-environments-security-and-logging)
   - [Module 3: Working with VS Code for Python Development](#module-3-working-with-vs-code-for-python-development)
   - [Module 4: Introduction to APIs](#module-4-introduction-to-apis)
   - [Module 5: Project Part 1 – Etherscan API and Wallet Balance Retrieval](#module-5-project-part-1--etherscan-api-and-wallet-balance-retrieval)
   - [Module 6: Logging Transactions and Data Management](#module-6-logging-transactions-and-data-management)
   - [Module 7: Storing Data with SQLite and Analyzing with NumPy](#module-7-storing-data-with-sqlite-and-analyzing-with-numpy)
   - [Final Project](#final-project)

---
 
# Project Overview

### Project Objectives

- Create a comprehensive code base and roadmap for tracking blockchain transactions.
- Develop a potential future course on crypto analytics and forensics.
- Enable students to create a crypto tracking application and roadmap for the course.
- Identify and resolve potential issues for future students.

### Student Goals

- Learn about basic Blochain interactrions, Crypto Fraud, and ways of identifying and analysizing blokchain data to identify fraud wallets
- Develop a crypto tracking application project and roadmap for a potential future course.
- Identify and resolve issues to streamline the course for future students.

### Student Tasks

- Research and determine the feasibility of tracking Bitcoin and Etherium using a private code base and basic crypto APIs.
- Develop a code base that can track Bitcoin transactions.
- Create a roadmap outlining the necessary skills for students to complete the course.

### Specific Expectations

- Assess the feasibility of the course for students and level of rigor (Undergraduate or Masters evel).
- Develop a code base for **tracking Bitcoin and Etherium** transactions.
- Create a roadmap detailing the skills required for the course.


# Roadmap
---

## Phase 1: Environment Setup ✓
1. **Create Environment and `.gitignore` for Etherscan API Key**
   - Set up a virtual environment for the project.
   - Create a `.gitignore` file to exclude sensitive information such as the Etherscan API key.
   - Create custom `logger_config.py` for program store logs in `crypto_analyis.log`

## Phase 2: Basic Functionality ✓
2. **Create `main.py` and Import Necessary Modules**
   - Initialize the main script file (`main.py`).
   - Import essential modules such as `requests`, `sqlite3`, `pandas`, and custom modules.
   - Create `api_module.py` for API use functionality
3. **Create Basic API Call for Single Wallet Balance**
   - Develop a function to fetch the balance of a single wallet address using the Etherscan API.
   - Integrate this function into `main.py` and test it.

4. **Create Multi-Address Balance Retrieval Feature**
   - Develop a function to fetch balances for multiple wallet addresses.
   - Integrate this function into `main.py` and test it.

## Phase 3: Transaction Tracking ✓
5. **Create Function to Fetch 'Normal' Transactions**
   - Develop a function to fetch a list of 'Normal' transactions for given addresses.
   - Integrate this function into `main.py` and test it.

## Phase 4: Data Storage and Organization ✓
6. **Store and Organize Transaction Data** 
   - Design a `database.py` (SQLite3) to store long term large data transaction details for each address into `etherscan_data.db`.
   - Pull long term big data from database and convert to Pandas Dataframe for faster analysis.

7. **Sort and Organize Transaction Data** 
   - Create `analysis.py` and develop an algorithm to sort and identify fraudulently connected addresses in the pandas dataframe transactions.
   - Run all the response wallet transaction data through this algorithm and indentify the string transactions and addresses connected to the root fraudulant address.

## Phase 5: Algorithmic Analysis and Data Visualization
8. **Create algorithm**
   - Create math model and documentaion for algorithm
   - Create a recursive traversal function to alanyze trasaction data and identify transaction history, root node(original address), and ending nodes (transaction ending adresses).

9. **Visualize Transactions**
   - Use a data visualization tool like NetworkX to visualize the transactions.
   - Create visual representations of the transaction data to identify patterns and insights.

## Phase 6: Documentation and Course Development
10. **Create Documentation**
   - Document the code base and provide clear instructions for setting up and running the project.
   - Create a detailed README file outlining the project objectives, setup instructions, and usage.

11. **Develop Course Roadmap**
   - Create a roadmap detailing the skills required for the course.
   - Outline the course structure, including modules, lessons, cumilative projects, and assignments.

# WORKFLOW 
---

1. Create ENV and `.gitignore` for Etherscan API key.
2. Create `main.py` and import necessary modules.
3. Create a basic API call to get the balance of a single wallet address.
4. Create a multi-address balance retrieval feature and integrate it into `main.py`.
5. Create a function to fetch a list of 'Normal' transactions for addresses and call it in `main.py`.
6. Create `database.py` & `etherscan_data.db` to store and organize transaction data using a data structure (long term big data SQLite database).
7. Develop an algorithm to sort and organize repeated sends and addresses in `analysis.py`.
8. Visualize the transactions using a data visualization tool like NetworkX or Matplotlib .

# Learning Pathway for Students

---

**Learning Path:**

1. Basic Python Programming: Start with simple programs like printing "Hello World", functions, loops, imports, classes, security precatuions (env./ gitignore), and finally github basics. Project 1: basic code crash course quizez and exam 

2. Learn about Ethereum and blockchain: Watch beginner-friendly tutorials or read articles to get a basic grasp of how Ethereum and transactions work. Very basic idea of what the blockchain actually is and functions and how we can 
use the provided public ledgers to track transactions 

3. APIs and JSON: Learn how to send requests to APIs and handle responses, starting with simple APIs before moving to Etherscan.A basic crash course on the structure of an API and what it's actuall doing when we run code. 
project 1: use blockcypher basic api to retreive the history of a coin using env's, a main.py, and a file with callable functions. 

4. SQLite Database: Learn how to set up a very simple database, then practice inserting, organizing, and retrieving data. 

5. Combine Concepts: Use Python to call the Etherscan API, extract transaction data, and store it in a database.


### **Crypto Analytics Course Outline v1 (Learning Path Detailed)**

#### **Course Overview:**
This course introduces students to the Python programming language, focusing on its application in blockchain analytics. Students will learn how to interact with blockchain APIs, manage data, and implement security best practices. By the end of the course, students will complete a comprehensive project that retrieves, stores, and analyzes blockchain data.



### **Module 1: Python Basics for Crypto Analytics (Part 1)**
**Objective**: Introduce the fundamentals of Python necessary for building blockchain projects.

**Topics Covered**:
1. **Basic Data Types**:
   - Integers, Strings, Floats, and Booleans.
2. **Control Structures**:
   - Loops: `for`, `while`.
   - Conditional Statements: `if`, `else`, `elif`.
3. **Functions**:
   - Defining and calling functions.
   - Function arguments and return values.
4. **Classes and OOP**:
   - Defining classes and creating objects.
   - Class methods and attributes.
5. **Imports**:
   - Using Python’s import system to bring in libraries.
6. **Code Structure**:
   - Writing modular and organized code, separating logic into functions or classes.

**Activity**: Write a Python script that calculates and displays a user's basic cryptocurrency holdings.

---

### **Module 2: Python Basics for Crypto Analytics (Part 2): Virtual Environments, Security, and Logging**
**Objective**: Combine the concepts of logging, virtual environments (venv), and security into a Python development workflow.

**Topics Covered**:
1. **Creating Virtual Environments (venv)**:
   - How to create and activate a virtual environment using `python -m venv`.
   - Installing dependencies using `pip`.
   - Managing a `requirements.txt` file.
   
2. **Common Security Practices**:
   - Using `.env` files to store sensitive data like API keys.
   - Securing Python projects by using `.gitignore` to hide sensitive files (e.g., API keys, configuration files).
   
3. **Logging in Python**:
   - Introduction to logging: why and how it’s used in development.
   - Setting up a logger in Python.
   - Logging levels: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`.
   - Logging to console and to files.
   
4. **Integrating Logging with the Project**:
   - Logging critical information like API requests, errors, and key actions within the program.
   - Properly organizing logs for easy debugging and tracking.

**Activity**:
1. Create and activate a virtual environment for the project.
2. Install necessary libraries (e.g., `requests` for API calls).
3. Implement logging to track basic program flow, such as logging successful API calls or errors when making requests.
4. Securely store the API key using a `.env` file and configure the program to load it securely.

---

### **Module 3: Working with VS Code for Python Development**
**Objective**: Teach students how to effectively use Visual Studio Code for Python development and file management.

**Topics Covered**:
1. **Basic File Management**:
   - Organizing and managing Python scripts in VS Code.
   - Creating and navigating through directories.
2. **Setting Up Python in VS Code**:
   - Installing the Python extension.
   - Running Python scripts directly from VS Code.
3. **Integrated Terminal**:
   - Using the terminal to activate virtual environments and run scripts.

**Activity**: Set up a simple project in VS Code, run a Python script, and manage virtual environments from within the terminal.

---

### **Module 4: Introduction to APIs**
**Objective**: Understand the basic structure of APIs and how to interact with them using Python.

**Topics Covered**:
1. **API Basics**:
   - What is an API, and how do APIs work?
   - Understanding `GET` and `POST` requests.
   - Introduction to JSON and parsing API responses.
2. **Making API Requests**:
   - Using Python's `requests` library to call APIs.
   - Understanding status codes and handling errors.
3. **Authentication**:
   - How to authenticate API requests with API keys.
   - How to handle API rate limits and timeouts.

**Activity**: Send an API request to a public cryptocurrency price API and parse the response to retrieve and display the current price of Ethereum.

---

### **Module 5: Project Part 1 – Etherscan API and Wallet Balance Retrieval**
**Objective**: Build a project that interacts with the Etherscan API to retrieve Ethereum wallet balances.

**Topics Covered**:
1. **Setting Up the Etherscan API**:
   - Register for an API key on Etherscan.
   - Overview of Etherscan’s API documentation.
2. **Making API Calls**:
   - Write Python code to request a balance for a specific Ethereum wallet.
   - Handle and format the API response.
3. **Logging API Requests**:
   - Log the API calls and their responses for debugging and record-keeping.
   - Log any API errors (such as rate limits or invalid requests).

**Activity**: Create a Python script that prompts the user for an Ethereum wallet address, retrieves the wallet balance using the Etherscan API, and logs the result.

---

### **Module 6: Logging Transactions and Data Management**
**Objective**: Extend the project by fetching transaction history and logging it for further analysis.

**Topics Covered**:
1. **Logging Transaction Records**:
   - Using the Etherscan API to retrieve transaction history for a wallet.
   - Storing transaction details (e.g., sender, receiver, value, and timestamp) in logs.
2. **Organizing Logs**:
   - Structuring log files for long-term projects.
   - Rotating logs for large projects.

**Activity**: Extend the previous project to log the transaction history of an Ethereum wallet to a file.

---

### **Module 7: Storing Data with SQLite and Analyzing with NumPy**
**Objective**: Store blockchain data in a SQLite database and perform basic analysis using NumPy.

**Topics Covered**:
1. **Introduction to SQLite**:
   - Creating and managing an SQLite database.
   - Creating tables and inserting data.
   - Writing queries to retrieve data.
2. **Storing API Data**:
   - Storing balance and transaction data from the API into the SQLite database.
3. **Data Analysis with NumPy**:
   - Using NumPy to perform basic analytics (e.g., summing up transaction values, finding averages).
   
**Activity**: Modify the project to store Ethereum wallet transaction history in SQLite and use NumPy to perform basic data analysis.

---

### **Final Project**
**Objective**: Combine all learned concepts into a final project that interacts with the Ethereum blockchain.

**Description**: Students will build a Python application that:
1. Retrieves wallet balances and transaction history from the Etherscan API.
2. Logs transaction records for analysis.
3. Stores retrieved data in a SQLite database.
4. Uses NumPy to perform basic data analytics on the stored transaction data (e.g., calculate total sent, total received, average transaction value).



