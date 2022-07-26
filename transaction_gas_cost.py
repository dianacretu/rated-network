# constant to convert wei to gwei
from_wei_to_gwei = 0.000000001

# function used to compute the gas cost in gwei for a transaction
def find_transaction_gas_cost(transaction_hash, dictionary):
    if not transaction_hash in dictionary:
        raise Exception("The transaction does not exist in the dataset.")

    transaction = dictionary[transaction_hash]

    # Using `receipt_gas_used * receipt_effective_gas_price` formula
    gas_cost_gwei = int(transaction.receipt_gas_used) * int(transaction.receipt_effective_gas_price) * from_wei_to_gwei

    return gas_cost_gwei