from decimal import Decimal
from termcolor import colored
from PyInquirer import prompt
from .get import get

def mint(currency_module):
    mint_data = prompt([
        {
            'type': 'input',
            'name': 'amount',
            'message': 'Enter the amount of tokens to  mint',
            'default': "1",
        },
        {
            'type': 'confirm',
            'name': 'confirmation',
            'message': 'Do you want to mint the selected tokens?',
            'default': False,
        },
    ])
    
    amount = Decimal(mint_data['amount']) * (10 ** get(currency_module)['decimals'])
    

    if mint_data['confirmation']:
        try:
            currency_module.mint(int(amount))
            print(colored('Tokens minted successfully!', 'green'))

        except Exception as e:
            print(colored('Tokens could not be minted. \n' + e, 'red'))

    else:
        print(colored('Tokens not minted!', 'blue'))