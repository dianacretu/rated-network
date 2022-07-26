import pytest
import transaction_gas_dollar_cost
from transaction import transaction
import transaction_gas_cost

# test to check if the take_coin_info_from_list returns the expected coin info
def test_take_coin_info_from_list_returns_value_as_expected():
    ethereum_info = {
                        "id": "ethereum",
                        "symbol": "eth",
                        "name": "Ethereum"
                    }

    assert ethereum_info == transaction_gas_dollar_cost.take_coin_info_from_list("Ethereum")

# test to check if the take_coin_info_from_list throws error when the coin does not exist
def test_take_coin_info_from_list_throws_error_when_coin_name_does_not_exist():
    with pytest.raises(Exception):
        transaction_gas_dollar_cost.take_coin_info_from_list("coin-does-not-exist-in-the list")

# test to check if the dollar cost of the gas used is as expected
def test_find_dollar_cost_of_gas_used_returns_value_as_expected():
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
        block_number=1, 
        block_hash='0x53c8aa1dc34b7ff5ab4e6df7ba95c9af3c0d72af5cb5a7a241609a3fc806701c', 
        max_fee_per_gas='43015358335', 
        max_priority_fee_per_gas='2984641665', 
        transaction_type='2', 
        receipt_effective_gas_price='32035059237')}

    # expected result is taken from Etherscan for the transaction with 0xd6ba7875aac43000e4e1b1b45dabb15e6ddc9b6fe862115f28ae4215c7319b24 hash
    gas_cost_gwei = 5977549843268778 * transaction_gas_cost.from_wei_to_gwei

    # default value for the timestamp of the block with number 0 taken from Etherscan
    first_block_timestamp = "30.07.2017 03:26:13 PM UTC"
    last_block_timestamp = "30.07.2017 03:26:23 PM UTC"
    last_block_number = 1
    eth_to_usd_for_timestamp = 197.19896347978235
    expectedResult = gas_cost_gwei * transaction_gas_dollar_cost.gwei_to_eth * eth_to_usd_for_timestamp

    actualResult = transaction_gas_dollar_cost.find_dollar_cost_of_gas_used('0x111', data_test, last_block_timestamp, last_block_number, "ethereum")

    assert expectedResult == actualResult