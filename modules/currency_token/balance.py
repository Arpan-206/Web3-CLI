from termcolor import colored
from.get import get

def balance(currency_module):
    details = get(currency_module)
    print(colored(f"The balance of current user is {currency_module.format_units(currency_module.balance(), details['decimals']) + ' ' + details['symbol']}.", 'green'))

def balance_of(currency_module, address):
    details = get(currency_module)
    print(colored(f"The balance of {address} is {currency_module.format_units(currency_module.balance_of(address), details['decimals']) + ' ' + details['symbol']}.", 'green'))