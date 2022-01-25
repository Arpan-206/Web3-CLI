import json

from PyInquirer import Separator, prompt
from termcolor import colored


def view(nft_module) -> None:
    """
    This function is used to view an NFT.
    """
    view_data = prompt([
        {
            'type': 'input',
            'name': 'id',
            'message': 'Enter the NFT ID',
            'default': "0",
        },
        {
            'type': 'list',
            'name': 'Print or Write to file?',
            'message': 'Do you want to print the NFT metadata or write it to a file?',
            'choices': [
                Separator('-- Print or Write to file --'),
                {
                    'name': 'Print',
                    'value': 'print',
                    'short': 'Print'
                },
                {
                    'name': 'Write to file',
                    'value': 'write',
                    'short': 'Write'
                }
            ]
        },
        {
            'type': 'input',
            'name': 'file_name',
            'message': 'Enter the file name (should be .json)',
            'default': "nft_metadata.json",
            'when': lambda answers: answers['Print or Write to file?'] == 'write',
            'validate': lambda answer: 'Please enter a valid file name' if not answer.endswith('.json') else True
        }
    ])
    id = int(view_data['id'])
    data = nft_module.get(id)
    data_dict = {"ID": str(id), "Name": data.name, "Description": data.description, "Image": str(
        data.image), "uri": data.uri, "Properties": data.properties}

    if view_data['Print or Write to file?'] == 'print':
        print(colored('NFT Data:', 'green'))
        for key, value in data_dict.items():
            print(colored(f'{key}: {value}', 'blue'))
    else:
        with open(view_data['file_name'], 'w') as f:
            f.write(json.dumps(data_dict))
        print(colored('NFT Metadata written to file successfully!', 'green'))
