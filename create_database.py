import sqlite3
from sqlite3 import Error
from transaction import transaction
import transaction_timestamp
import sys
import transaction_gas_cost
import transaction_gas_dollar_cost
import time

sql_create_table = """ CREATE TABLE IF NOT EXISTS processed_transactions (
                                        hash text PRIMARY KEY,
                                        fromAddress text,
                                        toAddress text,
                                        blockNumber text,
                                        executedAt text,
                                        gasUsed text,
                                        gasCostInDollars text
                                    ); """

# creates a table using the default sql_create_table statement
def create_table(conn):
    try:
        c = conn.cursor()
        c.execute(sql_create_table)
    except Error as e:
        print(e)

# creates a database connection to the SQLite database
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


# inserts the object received as an argument to the processed_transactions table
def insert_object_to_table(conn, object):
    sql = ''' INSERT INTO processed_transactions(hash,fromAddress,toAddress,blockNumber,executedAt,gasUsed,gasCostInDollars)
              VALUES(?,?,?,?,?,?,?) '''

    cur = conn.cursor()
    cur.execute(sql, object)
    conn.commit()
    return cur.lastrowid

# creates the object and inserts it to the table
def create_object_and_insert_to_table(key, data, conn, latest_block_timestamp, latest_block_number, coin_id):
    timestamp = transaction_timestamp.find_transaction_timestamp(key, data, latest_block_timestamp, latest_block_number)
    gasUsed = transaction_gas_cost.find_transaction_gas_cost(key, data)
    gasCostInDollars = transaction_gas_dollar_cost.find_dollar_cost_of_gas_used(key, data, latest_block_timestamp, latest_block_number, coin_id)

    object = (key, data[key].from_address, data[key].to_address, data[key].block_number, timestamp, gasUsed, gasCostInDollars)

    project_id = insert_object_to_table(conn, object)



# insert all the data to the table
def insert_data_to_table(conn, data, latest_block_timestamp, latest_block_number, coin_id):
    with conn:
        for key in data:
            create_object_and_insert_to_table(key, data, conn, latest_block_timestamp, latest_block_number, coin_id)

            # we need to wait 2 seconds between the requests to Coin Geko Api to not receive "Too many requests" error
            time.sleep(2)