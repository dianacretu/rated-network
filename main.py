from pydantic import BaseModel
import csv
from datetime import datetime
from transaction import transaction
import transaction_timestamp
import sys
import transaction_gas_cost
import transaction_gas_dollar_cost
from create_database import create_connection, create_table, insert_data_to_table
import time

args = sys.argv[1:]

# create a dictionary
data = {}

if len(args) == 0:
    raise Exception("You need to specify the file.")

file = args[0]
print(file)
with open(file, 'r') as csvf:
    csvReader = csv.DictReader(csvf)
         
    # add each row to the dictionary whose key is the transaction hash
    for rows in csvReader:
        tx = transaction(**rows)
        data[tx.hash] = tx

# date in string format
latest_block_timestamp = "26.07.2022 12:32:54 AM UTC"
latest_block_number = 15218113

coin_info = transaction_gas_dollar_cost.take_coin_info_from_list("Ethereum")


database = r"/home/siltros/RatedLabs/rated-network/pythonsqlite.db"

# create a database connection
conn = create_connection(database)

# create table
if conn is not None:
    # create projects table
    create_table(conn)
else:
    print("Error! cannot create the database connection.")

insert_data_to_table(data, conn, latest_block_timestamp, latest_block_number, coin_info["id"])