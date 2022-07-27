from shutil import ExecError
import pytest
from transaction import transaction
import transaction_gas_cost

# test to see if the find_transaction_gas_cost returns the expected result
def test_find_transaction_gas_cost_returns_value_as_expected():
    # we create a mock dictionary
    data_test = {'0x111': transaction(
        hash='0x111', 
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
        block_number=2, 
        block_hash='0x53c8aa1dc34b7ff5ab4e6df7ba95c9af3c0d72af5cb5a7a241609a3fc806701c', 
        max_fee_per_gas='43015358335', 
        max_priority_fee_per_gas='2984641665', 
        transaction_type='2', 
        receipt_effective_gas_price='32035059237')}

    # expected result is taken from Etherscan for the transaction with 0xd6ba7875aac43000e4e1b1b45dabb15e6ddc9b6fe862115f28ae4215c7319b24 hash
    expectedResult = 5977549843268778 * transaction_gas_cost.from_wei_to_gwei
    actualResult = transaction_gas_cost.find_transaction_gas_cost("0x111", data_test)

    assert expectedResult == actualResult
    
# test to see if the find_transaction_gas_cost throws error when transaction does not exist in the dictionary
def test_find_transaction_gas_cost_throws_error_when_transaction_does_not_exist():
    # we create a mock dictionary
    data_test = {'0x111': transaction(
        hash='0x111', 
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
        block_number=2, 
        block_hash='0x53c8aa1dc34b7ff5ab4e6df7ba95c9af3c0d72af5cb5a7a241609a3fc806701c', 
        max_fee_per_gas='43015358335', 
        max_priority_fee_per_gas='2984641665', 
        transaction_type='2', 
        receipt_effective_gas_price='32035059237')}
        
    with pytest.raises(Exception):
        transaction_gas_cost.find_transaction_gas_cost("0x0", data_test)
