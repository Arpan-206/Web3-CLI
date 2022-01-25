import sys

from PyInquirer import Separator, prompt
from termcolor import colored

from .nft_collection.burn import burn
from .nft_collection.mint import mint_prompt
from .nft_collection.transfer import transfer_prompt
from .nft_collection.view import view
from .nft_collection.view_by_owner import view_by_owner


def nft_collection(nft_module):
    """
    This is the main function of the NFT collection module. It will prompt you to select the action that you want to do on the NFT collection module. Then it will call the corresponding function and that function takes on. 
    """
    actions = prompt([
        {
            'type': 'list',
            'name': 'action',
            'message': 'What do you want to do?',
            'choices': [
                Separator('-- Actions --'),
                {
                    'name': 'Mint an NFT',
                    'value': 'mint',
                    'short': 'Mint'
                },
                {
                    'name': 'Transfer an NFT',
                    'value': 'transfer',
                    'short': 'Transfer'
                },
                {
                    'name': 'View an NFT',
                    'value': 'view',
                    'short': 'View'
                },
                {
                    'name': 'View all NFTs of a specific owner',
                    'value': 'view_by_owner',
                    'short': 'View By Owner'
                },
                {
                    'name': 'Burn an NFT',
                    'value': 'burn',
                    'short': 'Burn'
                }
            ]
        }
    ])

    if actions['action'] == 'mint':
        mint_prompt(nft_module=nft_module)

    elif actions['action'] == 'transfer':
        transfer_prompt(nft_module=nft_module)

    elif actions['action'] == 'view':
        view(nft_module=nft_module)

    elif actions['action'] == 'burn':
        burn(nft_module=nft_module)

    elif actions['action'] == 'view_by_owner':
        view_by_owner(nft_module=nft_module)
    else:
        print(colored('No Action Selected', 'red'))
        sys.exit(1)