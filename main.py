from pydantic import BaseModel
import csv
from datetime import datetime
from transaction import transaction 
import transaction_timestamp
import sys

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
transaction_hash = "0x0ba5abf4ef9eedb75a7fd5e645034288e02c6c4fafebf932e191b4df1f8ffac8"
print(transaction_timestamp.find_transaction_timestamp(transaction_hash, data, latest_block_timestamp, latest_block_number))
print(transaction_timestamp.find_transaction_timestamp_knowing_average_block_length(transaction_hash, data))

