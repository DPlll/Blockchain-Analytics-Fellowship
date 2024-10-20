#import data gathered from api and store it in the database into a pandas dataframe for analysis
import sqlite3
import pandas as pd
from Modules.logger_config import configure_logger

# Set up logger
logger = configure_logger(log_file='logs/crypto_analysis.log')

#connect to the database
conn = sqlite3.connect('database/etherscan_data.db')

#define the spl query to fetch all transactions
query = "SELECT * FROM transactions" #select all columns from the transactions table

#Load data from the database into a pandas dataframe
df = pd.read_sql_query(query,conn)

#close the database connection
conn.close()

# --- Display the Overview data ---
def display_overview(df):
    print(f" Data pulled from etherscan_data.db: \n{df.head(21)}") #display the first "x" rows of the dataframe
    print(f" Summary Statistics of Tracsactions: \n{df['tx_value'].describe()}" ) #display the summary statistics of the dataframe
    print(f"Count of null/empty values by column: \n{df.isnull().sum()}")  # Sum of null values per column
    print(f"Data Types: \n{df.info()}") # Display the data types of each column
display_overview(df)

# --- Clean the data ---







