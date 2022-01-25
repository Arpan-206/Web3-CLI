from decimal import Decimal

from PyInquirer import prompt
from termcolor import colored
from .get import get


def transfer(currency_module):
    transfer_data = prompt([
        {
            'type': 'input',
            'name': 'amount',
            'message': 'Enter the amount of tokens to  transfer',
            'default': "1",
        },
        {
            'type': 'input',
            'name': 'address',
            'message': 'Enter the address of the other account',
        },
        {
            'type': 'confirm',
            'name': 'confirmation',
            'message': 'Do you want to transfer the selected tokens?',
            'default': False,
        },
    ])

    amount = Decimal(transfer_data['amount']) * \
        (10 ** get(currency_module)['decimals'])

    if transfer_data['confirmation']:
        try:
            signer_addr = currency_module.get_signer_address()
            currency_module.set_allowance(signer_addr, amount)
            currency_module.transfer_from(signer_addr,
                transfer_data['address'], int(amount))
            print(colored('Tokens transferred successfully!', 'green'))

        except Exception as e:
            print(colored('Tokens could not be transferred. \n' + e, 'red'))
