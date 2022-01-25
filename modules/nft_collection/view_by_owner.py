# Importing the required modules
from PyInquirer import prompt, Separator
from termcolor import colored
import json

# Defining the view_by_owner function
def view_by_owner(nft_module) -> None:
    """
    This function is used to view all NFTs of a specific owner.
    """

    # Getting the owner address
    view_data = prompt([
        {
            'type': 'input',
            'name': 'owner',
            'message': 'Enter the Owners\'s Address',
        }, {
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

    # Fetching the owner address
    owner = view_data['owner']
    data = nft_module.get_owned(owner)

    # Printing the NFT metadata
    if view_data['Print or Write to file?'] == 'print':
        print(colored('NFTs owned by ' + owner + ':', 'green'))
        for i in range(len(data)):
            print(colored(
                f'{data[i].id}: Name: {data[i].name}, Description: { data[i].description }, Image: { data[i].image }, URL: { data[i].uri }', 'blue'))

    # Writing the NFT metadata to a file
    elif view_data['Print or Write to file?'] == 'write':
        data_dict = {}

        for i in range(len(data)):
            data_dict[str(i)] = {"ID": str(data[i].id), "Name": data[i].name, "Description": data[i].description, "Image": str(
                data[i].image), "uri": data[i].uri, "Properties": data[i].properties}

        with open(view_data['file_name'], 'w') as f:
            f.write(json.dumps(data_dict, indent=4))
