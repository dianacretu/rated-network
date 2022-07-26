from pydantic import BaseModel
import csv
from datetime import datetime
from transaction import transaction
import transaction_timestamp
import sys
import transaction_gas_cost

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

# calculate the timestamp for each transaction
for key in data:
    print(transaction_timestamp.find_transaction_timestamp(key, data, latest_block_timestamp, latest_block_number))

# calculate the gas cost in gwei for each transaction
for key in data:
    print(transaction_gas_cost.find_transaction_gas_cost(key, data))
