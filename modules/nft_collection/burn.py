# Importing the required modules
from PyInquirer import prompt
from termcolor import colored


# Defining the burn function
def burn(nft_module) -> None:
    """
    The function is used to burn an NFT.
    """

    # Getting the NFT to burn
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

    # Fetching the NFT id
    id = int(burn_data['id'])
    
    # Confirming the burn
    if burn_data['confirmation']:
        try:
            # Burning the NFT
            nft_module.burn(id)
            print(colored('NFT burned successfully!', 'green'))

        except Exception as e:
            # Printing the error
            print(colored('NFT could not be burned. \n' + e, 'red'))

    else:
        # Reporting if cancelled
        print(colored('NFT not burned!', 'blue'))
