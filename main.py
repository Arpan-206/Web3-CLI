# Importing stuff

import os

from dotenv import load_dotenv
from itsdangerous import exc

from pyfiglet import Figlet
from PyInquirer import Separator, prompt
from termcolor import colored
from thirdweb import MintArg, SdkOptions, ThirdwebSdk

from modules.mint import mint_prompt


# choose your network
network = "https://rinkeby-light.eth.linkpool.io/"
load_dotenv()
nft_smart_contract_address = "0xDc66c03Ed6E34933643680cb4D43e9caaE01A97A"
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
# create the object
sdk = ThirdwebSdk(SdkOptions(), network)
sdk.set_private_key(PRIVATE_KEY)

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
    }
])
try:
    nft_module = sdk.get_nft_module(nft_data['NFT Smart Contract Address'])
except exc.BadSignature:
    print(colored('Invalid NFT Smart Contract Address', 'red'))
    exit()

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
            }, {
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
                'value': 'view_all',
                'short': 'View All'
            },
            {
                'name': 'View an NFT\'s metadata',
                'value': 'view_metadata',
                'short': 'View Metadata'
            },
            {
                'name': 'View an NFT\'s image',
                'value': 'view_image',
                'short': 'View Image'
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
    mint_prompt(sdk=sdk, nft_module=nft_module)
