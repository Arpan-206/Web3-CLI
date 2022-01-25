from decimal import Decimal

from PyInquirer import prompt
from termcolor import colored
from thirdweb_web3.exceptions import TimeExhausted

from .get import get


def burn(currency_module):
    """
    This function is used to burn some tokens from your account.
    """

    # Get the amount of tokens to burn
    burn_data = prompt([
        {
            'type': 'input',
            'name': 'amount',
            'message': 'Enter the amount of tokens to  burn',
            'default': "1",
        },
        {
            'type': 'confirm',
            'name': 'confirmation',
            'message': 'Do you want to burn the selected tokens?',
            'default': False,
        },
    ])

    # Convert the amount to the correct decimal format
    amount = Decimal(burn_data['amount']) * \
        (10 ** get(currency_module)['decimals'])

    # Confirm the burn
    if burn_data['confirmation']:
        try:
            try:
                currency_module.burn(int(amount))
            except TimeExhausted:
                print(colored(
                    'A time exhaust has been detected. The tokens were most likely burnt. Please verify before trying again.', 'red'))
            print(colored('Tokens burned successfully!', 'green'))

        except Exception as e:
            print(colored('Tokens could not be burned. \n' + e, 'red'))

    else:
        print(colored('Tokens not burned!', 'blue'))
