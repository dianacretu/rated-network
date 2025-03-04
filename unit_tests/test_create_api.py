from unittest import mock
import pytest
from http import HTTPStatus
from fastapi.testclient import TestClient as Client
from create_database import create_connection, insert_object_to_table, create_table
from create_api import app, file_path, Item
import create_api
import random
import string
import json
import os

# test to check if get request returns the exepcted response
def test_get_item_returns_expected_reposnse_code_and_object():
     # Prevent pytest from trying to collect webtest's TestApp as tests:
    Client.__test__ = False
    client = Client(app)

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "test_db.db")
    create_api.file_path = filename
    conn = create_connection(create_api.file_path)

    create_table(conn)

    random_hash = ''.join(random.choice(string.ascii_letters) for i in range(20))
    item = create_api.Item(hash= random_hash, fromAddress= 'address', toAddress= "address", blockNumber= "12", executedAt= "any-date", gasUsed= "12", gasCostInDollars= "14")
    object = (random_hash, "address", "address", "12", "any-date", "12", "14")
    project_id = insert_object_to_table(conn, object)
    response = client.get("/transactions/" + random_hash)

    assert response.status_code == 200
    assert json.dumps(response.json()) == item.json()

# test to check if get requests returns 404 when hash not present in the table
def test_get_item_returns_404_when_hash_not_present():
     # Prevent pytest from trying to collect webtest's TestApp as tests:
    Client.__test__ = False

    client = Client(app)

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "test_db.db")
    create_api.file_path = filename
    conn = create_connection(create_api.file_path)

    create_table(conn)

    random_hash = ''.join(random.choice(string.ascii_letters) for i in range(20))
    item = create_api.Item(hash= random_hash, fromAddress= 'address', toAddress= "address", blockNumber= "12", executedAt= "any-date", gasUsed= "12", gasCostInDollars= "14")
    object = (random_hash, "address", "address", "12", "any-date", "12", "14")
    project_id = insert_object_to_table(conn, object)
    response = client.get("/transactions/" + '111001')

    assert response.status_code == 404