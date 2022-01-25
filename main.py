# Importing stuff

import os
import sys

from dotenv import load_dotenv
from pyfiglet import Figlet
from PyInquirer import Separator, prompt
from termcolor import colored
from thirdweb import SdkOptions, ThirdwebSdk

def main() -> None:
    f = Figlet(font='slant')
    credit = colored(
        '                              By Arpan Pandey\n', 'blue', attrs=['bold'])
    description = colored(
        f'A CLI tool to manage your own NFT Collection from the command line via the *thirdweb* platform.', 'cyan')
    print(colored(f.renderText('WEB3 CLI'), 'green'), credit, description, '\n')

    nft_data = prompt([
        {
            'type': 'list',
            'name': 'module',
            'message': 'Select the module you want to use',
            'choices': [
                Separator('-- Modules --'),
                {
                    'name': 'NFT Collection',
                    'value': 'nft_collection',
                    'short': 'NFT Collection'
                },
                {
                    'name': 'NFT Bundle',
                    'value': 'nft_bundle',
                    'short': 'NFT Bundle'
                },
                {
                    'name': 'Currency',
                    'value': 'currency',
                    'short': 'Currency'
                },
                {
                    'name': 'Pack',
                    'value': 'pack',
                    'short': 'Pack'
                }
            ]
        },
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

    except Exception:
        print(colored('Error In Data', 'red'))
        sys.exit(1)


    if nft_data['module'] == 'nft_collection':
        nft_module = sdk.get_nft_module(nft_data['NFT Smart Contract Address'])
        from modules.collection import nft_collection
        nft_collection(nft_module=nft_module)

    elif nft_data['module'] == 'currency':
        currency_module = sdk.get_currency_module(nft_data['NFT Smart Contract Address'])
        from modules.currency import currency
        currency(currency_module=currency_module)

    else:
        print(colored('No Module Selected', 'red'))


if __name__ == '__main__':
    main()
