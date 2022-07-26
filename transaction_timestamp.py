from datetime import datetime, timedelta

# default value for the timestamp of the block with number 0 taken from Etherscan
first_block_timestamp = "30.07.2015 03:26:13 PM UTC"

# default average block length
average_block_length = 13

# function used to find the timestamp of a transaction without knowing the average block length
# we need the latest block timestamp and latest block number in order to calculate the average block length
def find_transaction_timestamp(transaction_hash, dictionary, latest_blob_timestamp, latest_block_number):
    if not transaction_hash in dictionary:
        raise Exception("The transaction does not exist in the dataset.")

    transaction = dictionary[transaction_hash]

    t1 = datetime.strptime(first_block_timestamp, '%d.%m.%Y %I:%M:%S %p %Z')
    t2 = datetime.strptime(latest_blob_timestamp, '%d.%m.%Y %I:%M:%S %p %Z')

    # get difference between timestamp of the latest block and timestamp of the first block
    delta = t2 - t1

    # find the average block length
    avg = delta.total_seconds()/latest_block_number

    # calculate the approximate timestamp for the transaction
    transaction_timestamp = t1 + timedelta(seconds=transaction.block_number * avg)

    return transaction_timestamp

# function used to find the timestamp of a transaction using the default average block length
def find_transaction_timestamp_knowing_average_block_length(transaction_hash, dictionary):
    if not transaction_hash in dictionary:
        raise Exception("The transaction does not exist in the dataset.")

    transaction = dictionary[transaction_hash]

    t1 = datetime.strptime(first_block_timestamp, '%d.%m.%Y %I:%M:%S %p %Z')

    # calculate the approximate timestamp for the transaction
    transaction_timestamp = t1 + timedelta(seconds=transaction.block_number * average_block_length)

    return transaction_timestamp