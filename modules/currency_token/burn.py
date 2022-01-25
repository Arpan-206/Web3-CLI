from decimal import Decimal

from PyInquirer import prompt
from termcolor import colored
from .get import get
from thirdweb_web3.exceptions import TimeExhausted


def burn(currency_module):
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

    amount = Decimal(burn_data['amount']) * \
        (10 ** get(currency_module)['decimals'])

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
