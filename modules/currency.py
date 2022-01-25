from PyInquirer import Separator, prompt


def currency(currency_module):
    """
    This module prompts you to select the action that you want to do on the currency module. Then it will call the corresponding function and that function takes on.
    """

    # This is the list of the actions that you can do on the currency module.
    actions = prompt([
        {
            'type': 'list',
            'name': 'action',
            'message': 'What do you want to do?',
            'choices': [
                Separator('-- Actions --'),
                {
                    'name': 'See the balance of your account',
                    'value': 'balance',
                    'short': 'Balance'
                },
                {
                    'name': 'Transfer some tokens to another account',
                    'value': 'transfer',
                    'short': 'Transfer'
                },
                {
                    'name': 'Burn some tokens',
                    'value': 'burn',
                    'short': 'Burn'
                },
                {
                    'name': 'See the balance of another account',
                    'value': 'balance_other',
                    'short': 'Balance Other'
                },
                {
                    'name': 'Get the value of a given amount of tokens',
                    'value': 'value',
                    'short': 'Value'
                },
                {
                    'name': 'Get the total supply of tokens',
                    'value': 'total_supply',
                    'short': 'Total Supply'
                },
                {
                    'name': 'Mint some tokens',
                    'value': 'mint',
                    'short': 'Mint'
                }
                
            ]
        },
        {
            'type': 'input',
            'name': 'address',
            'message': 'Enter the address of the other account',
            'when': lambda answers: answers['action'] == 'balance_other'
        }
    ])

    # Calling the desired function.
    if actions['action'] == 'balance':
        from .currency_token.balance import balance
        balance(currency_module)

    elif actions['action'] == 'balance_other':
        from .currency_token.balance import balance_of
        balance_of(currency_module, actions['address'])

    elif actions['action'] == 'mint':
        from .currency_token.mint import mint
        mint(currency_module)

    elif actions['action'] == 'transfer':
        from .currency_token.transfer import transfer
        transfer(currency_module)

    elif actions['action'] == 'value':
        from .currency_token.value import value
        value(currency_module)

    elif actions['action'] == 'burn':
        from .currency_token.burn import burn
        burn(currency_module)

    elif actions['action'] == 'total_supply':
        from .currency_token.supply import supply
        supply(currency_module)

    else:
        raise Exception('Invalid action')