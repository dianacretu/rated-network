import pytest
import os.path
from create_database import create_connection, create_table, insert_data_to_table
from transaction import transaction
import random
import string

# test to check if the database is created
def test_create_database_creates_database_file():
    dirname = os.path.dirname(__file__)
    file_path = os.path.join(dirname, "test_db.db")

    create_connection(file_path)

    assert os.path.exists(file_path)

# test to check if the table is created
def test_create_table_function_creates_a_table():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "test_db.db")
    file_path = filename
    #file_path = r"~/RatedLabs/rated-network/unit_tests/test_db.db"
    conn = create_connection(file_path)

    create_table(conn)

    sql_create_table = """ SELECT name FROM sqlite_master WHERE type='table' AND name='processed_transactions'; """

    cur = conn.cursor()
    tables = cur.execute(sql_create_table)

    assert len(tables.fetchall())> 0

# test to check if we insert the data in the table
def test_insert_data_to_table_wroks_as_expected():
    random_hash = ''.join(random.choice(string.ascii_letters) for i in range(20))
    # we create a mock dictionary
    data_test = {random_hash: transaction(
        hash= random_hash, 
        nonce=3, 
        transaction_index='117', 
        from_address='0x75', 
        to_address='0x8ed', 
        value='4000', 
        gas='21000', 
        gas_price='23871340807', 
        input='0x', 
        receipt_cumulative_gas_used='8784826', 
        receipt_gas_used='186594', 
        receipt_contract_address='', 
        receipt_root='', 
        receipt_status='1', 
        block_number=1, 
        block_hash='0x53c8aa1dc34b7ff5ab4e6df7ba95c9af3c0d72af5cb5a7a241609a3fc806701c', 
        max_fee_per_gas='43015358335', 
        max_priority_fee_per_gas='2984641665', 
        transaction_type='2', 
        receipt_effective_gas_price='32035059237')}

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "test_db.db")
    file_path = filename

    conn = create_connection(file_path)

    create_table(conn)

    insert_data_to_table(conn, data_test, "30.07.2017 03:26:13 PM UTC", 1, "ethereum")

    sql_create_table = """ SELECT * FROM processed_transactions; """

    cur = conn.cursor()
    tables = cur.execute(sql_create_table)

    assert len(tables.fetchall()) > 0

