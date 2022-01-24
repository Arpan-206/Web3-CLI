# Importing stuff

import os
import sys

from dotenv import load_dotenv
from pyfiglet import Figlet
from PyInquirer import Separator, prompt
from termcolor import colored
from thirdweb import SdkOptions, ThirdwebSdk

from modules.mint import mint_prompt
from modules.transfer import transfer_prompt
from modules.view import view
from modules.burn import burn
from modules.view_by_owner import view_by_owner

f = Figlet(font='slant')
credit = colored(
    '                              By Arpan Pandey\n', 'blue', attrs=['bold'])
description = colored(
    f'A CLI tool to manage your own NFT Collection from the command line via the *thirdweb* platform.', 'cyan')
print(colored(f.renderText('NFT CLI'), 'magenta'), credit, description, '\n')

nft_data = prompt([
    {
        'type': 'input',
        'name': 'NFT Smart Contract Address',
        'message': 'Enter the NFT Smart Contract Address',
        'validate': lambda val: val != ''
    },
    {
        'type': 'input',
        'name': 'Network URL',
        'message': 'Enter the Network URL',
        'default': "https://rinkeby-light.eth.linkpool.io/",
    },
    {
        'type': 'list',
        'name': 'Where is the Private Key?',
        'message': 'Where is the Private Key?',
        'choices': [
            Separator('-- Where is the Private Key? --'),
            {
                'name': 'In the Environment',
                'value': 'env'
            },
            {
                'name': 'I will provide it in the next step',
                'value': 'next_step'
            }
        ]
    },
    {
        'type': 'password',
        'name': 'Private Key',
        'message': 'Enter the Private Key',
        'when': lambda answers: answers['Where is the Private Key?'] == 'next_step',
        'validate': lambda val: val != ''
    }
])
try:
    network = nft_data['Network URL']
    sdk = ThirdwebSdk(SdkOptions(
        ipfs_gateway_url='https://cloudflare-ipfs.com/ipfs/'), network)
    if nft_data['Where is the Private Key?'] == 'env':
        load_dotenv()
        PRIVATE_KEY = os.getenv("PRIVATE_KEY")
        if PRIVATE_KEY is None:
            print(colored(
                'No private key found in the environment. make sure it is saved as `PRIVATE_KEY={Your Private Key}` in and `.env` file.', 'red'))
            sys.exit(1)
    else:
        PRIVATE_KEY = nft_data['Private Key']
    sdk.set_private_key(PRIVATE_KEY)
    nft_module = sdk.get_nft_module(nft_data['NFT Smart Contract Address'])

except Exception:
    print(colored('Error In Data', 'red'))
    sys.exit(1)

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

def main():
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

if __name__ == '__main__':
    main()