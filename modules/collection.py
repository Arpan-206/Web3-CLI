import sys

# Importing the required modules
from PyInquirer import Separator, prompt
from termcolor import colored


def nft_collection(nft_module):
    """
    This is the main function of the NFT collection module. It will prompt you to select the action that you want to do on the NFT collection module. Then it will call the corresponding function and that function takes on. 
    """

    # This is the list of the actions that you can do on the NFT collection module.
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

    # Calling the corresponding function based on the action that you selected.
    if actions['action'] == 'mint':
        from .nft_collection.mint import mint_prompt
        mint_prompt(nft_module=nft_module)

    elif actions['action'] == 'transfer':
        from .nft_collection.transfer import transfer_prompt
        transfer_prompt(nft_module=nft_module)

    elif actions['action'] == 'view':
        from .nft_collection.view import view
        view(nft_module=nft_module)

    elif actions['action'] == 'burn':
        from .nft_collection.burn import burn
        burn(nft_module=nft_module)

    elif actions['action'] == 'view_by_owner':
        from .nft_collection.view_by_owner import view_by_owner
        view_by_owner(nft_module=nft_module)

    else:
        print(colored('No Action Selected', 'red'))
        sys.exit(1)