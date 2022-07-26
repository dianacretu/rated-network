from pydantic import BaseModel
import csv
from datetime import datetime

class transaction(BaseModel):
    hash: str
    nonce: int
    transaction_index: str
    from_address: str
    to_address: str
    value: str
    gas: str
    gas_price: str
    input: str
    receipt_cumulative_gas_used: str
    receipt_gas_used: str
    receipt_contract_address: str
    receipt_root: str
    receipt_status: str
    block_number: int
    block_hash: str
    max_fee_per_gas: str
    max_priority_fee_per_gas: str
    transaction_type: str
    receipt_effective_gas_price: str