from pycoingecko import CoinGeckoAPI
import datetime
import transaction_gas_cost
import transaction_timestamp

default_currency = "usd"
gwei_to_eth = 0.00000000185 

# function which returns the coin info knowing the name of the coin from the list of all coins
def take_coin_info_from_list(coin_name):
    coin_api = CoinGeckoAPI()

    coin_list = coin_api.get_coins_list()

    coin_info = {'id':"no-coin"}
    for element in coin_list:
        if element['name'] == coin_name:
            coin_info = element

    if coin_info["id"] == "no-coin":
        raise Exception("No coin with name " + coin_name + " was found in the list.")

    return coin_info

# function which returns the price of the coin with the id taken as parameter in the default currency
def find_coin_price_in_currency_at_transaction_time(id, transaction_time):
    coin_api = CoinGeckoAPI()

    time = str(transaction_time.day) + "-" + str(transaction_time.month) + "-" + str(transaction_time.year)
    history = coin_api.get_coin_history_by_id(id, time)

    return history["market_data"]["current_price"][default_currency]

# function which computes the gas cost in the default currency (usd)
def find_dollar_cost_of_gas_used(transaction_hash, data, latest_block_timestamp, latest_block_number, coin_id):
    gas_cost_gwei = transaction_gas_cost.find_transaction_gas_cost(transaction_hash, data)
    transaction_time = transaction_timestamp.find_transaction_timestamp(transaction_hash, data, latest_block_timestamp, latest_block_number)

    eth_price_in_default_currency = find_coin_price_in_currency_at_transaction_time(coin_id, transaction_time)
    gas_cost_eth = gas_cost_gwei * gwei_to_eth
    gas_cost_default_currency = gas_cost_eth * eth_price_in_default_currency

    return gas_cost_default_currency