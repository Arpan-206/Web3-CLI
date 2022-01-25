# Importing the required modules
from PyInquirer import prompt
from thirdweb_web3.exceptions import ContractLogicError
from termcolor import colored

def transfer_prompt(nft_module) -> None:
    """
    This function is used to transfer an NFT.
    """
    # Getting the NFT to transfer
    transfer_args = prompt([
        {
            'type': 'input',
            'name': 'to',
            'message': 'Who should receive the NFT?',
        },
        {
            'type': 'input',
            'name': 'id',
            'message': 'NFT Token ID',
            'default': '0'
        },
    ])
    try:
        # Trying to execute the transfer
        nft_module.transfer(to_address=transfer_args['to'],
                            token_id=transfer_args['id'],)
    except ContractLogicError:
        # Printing the error if the transfer failed
        print(colored('Error: Either you do not own the NFT or some other error has occurred.', 'red'))
        return

    # Printing the success message
    print(colored('NFT transferred successfully!\n', 'green'))
