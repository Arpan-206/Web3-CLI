from termcolor import colored
from .get import get
from decimal import Decimal

def supply(currency_module):
    try:
        total_supply = Decimal(currency_module.total_supply() / (10 ** get(currency_module)['decimals']))
        print(colored(
            f"Total supply of {get(currency_module)['symbol']} is {total_supply}", 'green'))

    except Exception as e:
        print(colored('Can\'t get total supply \n' + e, 'red'))
