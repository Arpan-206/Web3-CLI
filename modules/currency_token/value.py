from decimal import Decimal

from PyInquirer import prompt
from termcolor import colored
from .get import get


def value(currency_module):
    """
    This function is used to get the value of the currency.
    """
    value_data = prompt([
        {
            'type': 'input',
            'name': 'amount',
            'message': 'Enter the amount of tokens to  get the value of',
            'default': "1",
        },
    ])

    amount = Decimal(value_data['amount']) * \
        (10 ** get(currency_module)['decimals'])

    try:
        print(colored( f"Value of {value_data['amount']} {get(currency_module)['symbol']}s is {currency_module.get_value(int(amount)).value} and its display value is {currency_module.get_value(int(amount)).display_value}", 'green'))

    except Exception as e:
        print(colored('Can\'t get value \n' + e, 'red'))
