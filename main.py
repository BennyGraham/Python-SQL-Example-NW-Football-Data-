
# Online Python - IDE, Editor, Compiler, Interpreter
# Navigate to https://www.online-python.com/ to copy, paste, and run code

# Program which stores raw data, creates a sql databse, and querys a result in browser memory or phyiscal ram


# Sql module native to Python Env

import sqlite3

# import panda module native to Python Env

import pandas as pd

# Create container for SQL Database Server

conn = sqlite3.connect('file:cachedb?mode=memory&cache=shared')


# Connect to SQL database in memory

cur  = conn.cursor()

# Load data frame with sample data using pandas

df = pd.DataFrame(
    
    {
                
"Game":[1,2,3,4,5],
"H_A":["Home","Home","Away","Home","Away"],
"Result":["L (21-38)","W (24-6)","L (23-30)","W (35-6)","L (7-56)"],
"PassCmp":[30,9,19,12,25],

"CmpPct":[69.8,56.3,48.7,60,62.5],
"PassYds":[283,66,260,88,256],
"PassTD":[3,1,2,0,1],
 "Opponent":["Michigan State","Indiana State","Duke","Ohio","Nebraska"]

    }
)

# Add table to database
df.to_sql("NWfbData", conn, if_exists="replace", index=False) 

# Query database and load result into dataframe
df = pd.read_sql_query("select * from NWfbData where PassTD = 1", conn) 

# Print query result in terminal
print (df)
