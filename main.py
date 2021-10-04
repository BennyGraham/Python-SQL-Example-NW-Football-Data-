
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
"Home_Away":["Home","Home","Away","Home","Away"],
"Opponent":["Michigan State","Indiana State","Duke","Ohio","Nebraska"],
"Result":["L (21-38)","W (24-6)","L (23-30)","W (35-6)","L (7-56)"],
"Pass_Cmp":[30,9,19,12,25],
"Pass_Att":[43,16,39,20,40],
"Cmp_Pct":[69.8,56.3,48.7,60,62.5],
"Pass_Yds":[283,66,260,88,256],
"Pass_TD":[3,1,2,0,1]

    }
)

# Add table to database
df.to_sql("NWfbData", conn, if_exists="replace") 

# Query database and load result into dataframe
df = pd.read_sql_query("select * from NWfbData where TD = 1", conn) 

# Print query result in terminal
print (df)
