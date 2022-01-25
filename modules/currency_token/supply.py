# Importing modules
from decimal import Decimal

from termcolor import colored

from .get import get


# The function to get the supply
def supply(currency_module):
    """
    This function is used to get the total supply of the currency.
    """
    try:
        total_supply = Decimal(currency_module.total_supply(
        ) / (10 ** get(currency_module)['decimals']))
        print(colored(
            f"Total supply of {get(currency_module)['symbol']} is {total_supply}", 'green'))

    except Exception as e:
        print(colored('Can\'t get total supply \n' + e, 'red'))
