from PyInquirer import prompt
from termcolor import colored


def burn(nft_module):
    burn_data = prompt([
        {
            'type': 'input',
            'name': 'id',
            'message': 'Enter the NFT ID',
            'default': "0",
        },
        {
            'type': 'confirm',
            'name': 'confirmation',
            'message': 'Do you want to burn the selected NFT?',
            'default': False,
        },

    ])
    id = int(burn_data['id'])
    
    if burn_data['confirmation']:
        try:
            nft_module.burn(id)
            print(colored('NFT burned successfully!', 'green'))

        except Exception as e:
            print(colored('NFT could not be burned. \n' + e, 'red'))

    else:
        print(colored('NFT not burned!', 'blue'))
