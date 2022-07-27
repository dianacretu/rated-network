import csv
from transaction import transaction
import sys
import transaction_gas_dollar_cost
from create_database import create_connection, create_table, insert_data_to_table
import os

args = sys.argv[1:]

# create a dictionary
data = {}

if len(args) == 0:
    raise Exception("You need to specify the file.")

file = args[0]

with open(file, 'r') as csvf:
    csvReader = csv.DictReader(csvf)
         
    # add each row to the dictionary whose key is the transaction hash
    for rows in csvReader:
        tx = transaction(**rows)
        data[tx.hash] = tx

# values for latest_block taken from Etherscan
latest_block_timestamp = "26.07.2022 12:32:54 AM UTC"
latest_block_number = 15218113

coin_info = transaction_gas_dollar_cost.take_coin_info_from_list("Ethereum")

if len(args) == 1:
    raise Exception("You need to specify the database file.")

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, args[1])
database = filename

# create a database connection
conn = create_connection(database)

# create table
if conn is not None:
    # create processed_transactions table
    create_table(conn)
else:
    raise Exception("Cannot create the database connection.")

insert_data_to_table(conn, data, latest_block_timestamp, latest_block_number, coin_info["id"])