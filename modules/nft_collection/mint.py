# Importing all the required modules
import io
from typing import *

import requests
from PIL import Image
from PyInquirer import Separator, prompt
from termcolor import colored
from thirdweb import MintArg
from thirdweb_web3.exceptions import TransactionNotFound


# Defining the mint function
def mint(nft_module, name: str, description: str, image_uri: str, image_format='JPEG', properties={}) -> str:
    """
    This function is used to mint an NFT.
    """
    # Checking if the image_uri is a local file or a remote file.
    if image_format != 'URL':
        try:
            if image_uri == '':
                byte_im = b''
            else:
                try:
                    # If the image_uri is a local file, then we will read the file and convert it to a byte array.
                    im = Image.open(image_uri)
                    byte_im = io.BytesIO()
                    im.save(byte_im, format=image_format)
                    byte_im = byte_im.getvalue()
                    nft_module.mint(MintArg(name=name,
                                            description=description,
                                            image_uri=byte_im,
                                            properties=properties))
                    im_resize = im.resize((500, 500))
                    buf = io.BytesIO()
                    im_resize.save(buf, format=image_format)
                    byte_im = buf.getvalue()

                except FileNotFoundError:
                    # File not found error.
                    print('File not found')
                    return  

            # Minting the NFT
            nft_module.mint(MintArg(name=name,
                                    description=description,
                                    image_uri=byte_im,
                                    properties=properties))

        except requests.exceptions.ReadTimeout:
            return 'A time out has occured. But, in most cases this is not a problem and the NFT is minted anyway. So, try to cross check before trying again.\n'

    else:
        # If the image_uri is a URL, then we will pass it straight on.
        nft_module.mint(MintArg(name=name,
                                    description=description,
                                    image_uri=image_uri,
                                    properties=properties))
    
    return 'NFT minted successfully!\n'

def mint_prompt(nft_module) -> None:
    mint_args = prompt([
        {
            'type': 'input',
            'name': 'name',
            'message': 'Name of the NFT',
            'validate': lambda name: name != ''
        },
        {
            'type': 'input',
            'name': 'description',
            'message': 'Description of the NFT',
        },
        {
            'type': 'list',
            'name': 'image_format',
            'message': 'Image Format',
            'choices': [
                Separator('-- Image Formats --'),
                {
                    'name': 'JPEG',
                    'value': 'JPEG',
                    'short': 'JPEG'
                },
                {
                    'name': 'PNG',
                    'value': 'PNG',
                    'short': 'PNG'
                },
                {
                    'name': 'URL',
                    'value': 'URL',
                    'short': 'URL'
                }
            ]
        },
        {
            'type': 'input',
            'name': 'image_uri',
            'message': 'URI of the NFT Image'
        },
        {
            'type': 'input',
            'name': 'properties',
            'message': 'Properties of the NFT',
            'default': '{}'
        }
    ])

    try:
        # Executinh the mint function
        print(colored(mint(nft_module=nft_module, name=mint_args['name'],
                           description=mint_args['description'], image_uri=mint_args[
                               'image_uri'], image_format=mint_args['image_format'],
                           properties=eval(mint_args['properties'])), 'green'))
    except TransactionNotFound:
        # Handling an error that sometimes occurs even when the NFT is minted.
        print(colored('Transaction not found. This is most likely because the transaction is not mined yet. Try fetching the NFT in a few seconds, most likely the transaction would have passed and you wouldn\'t need to mint again.', 'yellow'))
