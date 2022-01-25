from termcolor import colored
from.get import get

def balance(currency_module) -> None:
    """
    This function is used to get your own current balance, i.e, get the number of tokens that you hold.
    """
    details = get(currency_module)
    print(colored(f"The balance of current user is {currency_module.format_units(currency_module.balance(), details['decimals']) + ' ' + details['symbol']}.", 'green'))

def balance_of(currency_module, address) -> None:
    """
    This module is used to get your someone's current balance, i.e, get the number of tokens that you hold.
    """
    details = get(currency_module)
    print(colored(f"The balance of {address} is {currency_module.format_units(currency_module.balance_of(address), details['decimals']) + ' ' + details['symbol']}.", 'green'))