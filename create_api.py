from numpy import block
from create_database import create_connection, create_table
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
file_path = r"/home/siltros/RatedLabs/rated-network/pythonsqlite.db"

class Item(BaseModel):
    hash: str
    fromAddress: str
    toAddress: str
    blockNumber: str
    executedAt: str
    gasUsed: str
    gasCostInDollars: str

@app.get("/transactions/{transaction_hash}", response_model=Item)
def read_item(transaction_hash: str):
    conn = create_connection(file_path)

    create_table(conn)

    sql_create_table = """ SELECT * FROM processed_transactions WHERE hash=?; """
    cur = conn.cursor()
    object = (transaction_hash,)
    
    tables = cur.execute(sql_create_table, object)

    records = cur.fetchall()
    
    if not len(records) == 1:
        raise HTTPException(status_code=404, detail="Transaction hash " + transaction_hash + " does not exist in the database.")

    item = Item(hash = records[0][0],fromAddress= records[0][1], toAddress=records[0][2], blockNumber=records[0][3], executedAt=records[0][4], gasUsed=records[0][5], gasCostInDollars=records[0][6])

    return item
