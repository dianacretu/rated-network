import pytest
from transaction import transaction
import transaction_timestamp
from datetime import datetime, timedelta

# test to see if the find_transaction_timestamp returns the expected result
def test_find_transaction_timestamp_returns_value_as_expected():
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
		receipt_gas_used='21000', 
		receipt_contract_address='', 
		receipt_root='', 
		receipt_status='1', 
		block_number=2, 
		block_hash='0x53c8aa1dc34b7ff5ab4e6df7ba95c9af3c0d72af5cb5a7a241609a3fc806701c', 
		max_fee_per_gas='43015358335', 
		max_priority_fee_per_gas='2984641665', 
		transaction_type='2', 
		receipt_effective_gas_price='23871340807')}

	last_block_date = "30.07.2015 03:28:23 PM UTC"
	block_number = 10

	# since we are looking for the timestamp of a transaction from block 2, we calculate the average block length
	# which is ("30.07.2015 03:28:23 PM UTC" - "30.07.2015 03:26:13 PM UTC")/10 = 2 min and 10 seconds /10= 130 seconds/10 = 13 seconds average block lenght
	# Since we are looking for the transaction from block 2, "30.07.2015 03:26:13 PM UTC" + 13s * 2 = "30.07.2015 03:26:39 PM UTC"
	expectedResult = datetime.strptime("30.07.2015 03:26:39 PM UTC", '%d.%m.%Y %I:%M:%S %p %Z')
	actualResult = transaction_timestamp.find_transaction_timestamp("0x111", data_test, last_block_date, block_number)
	
	assert expectedResult == actualResult

# test to see if the find_transaction_timestamp_knowing_average_block_length returns the expected result
def test_find_transaction_timestamp_knowing_average_block_length_returns_value_as_expected():
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
		receipt_gas_used='21000', 
		receipt_contract_address='', 
		receipt_root='', 
		receipt_status='1', 
		block_number=2, 
		block_hash='0x53c8aa1dc34b7ff5ab4e6df7ba95c9af3c0d72af5cb5a7a241609a3fc806701c', 
		max_fee_per_gas='43015358335', 
		max_priority_fee_per_gas='2984641665', 
		transaction_type='2', 
		receipt_effective_gas_price='23871340807')}

	# we know that the average block length is 13 since we are using the default value
	# since we are looking for the transaction from block 2, "30.07.2015 03:26:13 PM UTC" + 13s * 2 = "30.07.2015 03:26:39 PM UTC"
	expectedResult = datetime.strptime("30.07.2015 03:26:39 PM UTC", '%d.%m.%Y %I:%M:%S %p %Z')
	resultFindTransactionTimestampKnowingAverage = transaction_timestamp.find_transaction_timestamp_knowing_average_block_length("0x111", data_test)
	
	assert resultFindTransactionTimestampKnowingAverage == expectedResult

# find_transaction_timestamp should throw error when the transaction is not present in the dictionary
def test_find_transaction_timestamp_throws_error_when_transaction_does_not_exist():

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
		receipt_gas_used='21000', 
		receipt_contract_address='', 
		receipt_root='', 
		receipt_status='1', 
		block_number=2, 
		block_hash='0x53c8aa1dc34b7ff5ab4e6df7ba95c9af3c0d72af5cb5a7a241609a3fc806701c', 
		max_fee_per_gas='43015358335', 
		max_priority_fee_per_gas='2984641665', 
		transaction_type='2', 
		receipt_effective_gas_price='23871340807')}
	
	with pytest.raises(Exception) as e_info:
		resultFindTransactionTimestamp = transaction_timestamp.find_transaction_timestamp("0x0", data_test, "any-string", 2)
	
# find_transaction_timestamp_knowing_average_block_length should throw error when the transaction is not present in the dictionary
def test_find_transaction_timestamp_knowing_average_block_length_throws_error_when_transaction_does_not_exist():

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
		receipt_gas_used='21000', 
		receipt_contract_address='', 
		receipt_root='', 
		receipt_status='1', 
		block_number=2, 
		block_hash='0x53c8aa1dc34b7ff5ab4e6df7ba95c9af3c0d72af5cb5a7a241609a3fc806701c', 
		max_fee_per_gas='43015358335', 
		max_priority_fee_per_gas='2984641665', 
		transaction_type='2', 
		receipt_effective_gas_price='23871340807')}
	
	with pytest.raises(Exception) as e_info:
		resultFindTransactionTimestamp = transaction_timestamp.find_transaction_timestamp_knowing_average_block_length("0x0", data_test)
	