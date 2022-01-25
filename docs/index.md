# Welcome to WEB3 CLI
This is a Command Line program to interact with your NFTs, Cryptocurrencies etc. via the [ThirdWeb Platform](https://thirdweb.com). This is just a fun little project that I made to be able to connect to blockchains and Web3 from the command line.

## Modules    
These are the modules that are currently supported, I will add more as I can.

* **Currency**- This module can be used to do all sorts of things like Minting new tokens, burning tokens, viewing the supply, transferring tokens etc.

* **NFT Collection**- This module can be used to mint NFTs, transfer NFTs, view NFT data etc.

## Project layout
This is the project file structure for reference.

    docs/
        index.md
    docs_assets/
        images/
            favicon.ico
        javascripts/
            config.js
        stylesheets/
            pdf-export.css
        theme/
            main.html
    modules/
        currency_token/
            balance.py
            burn.py
            get.py
            mint.py
            supply.py
            transfer.py
            value.py
        nft_collection/
            burn.py
            mint.py
            transfer.py
            view_by_owner.py
            view.py
        collection.py
        currency.py
    .gitignore
    docs-requirements.txt
    main.py
    mkdocs.yml
    requirements.txt

# Dependencies
This program depends on the following dependencies. Huge shoutout to all the maintainers and contributors of these packages.  

* [PyInquirer](https://github.com/CITGuru/PyInquirer)
* [termcolor](https://pypi.org/project/termcolor/)
* [thirdweb-sdk](https://thirdweb.com)
* [python-dotenv](https://pypi.org/project/python-dotenv/)
* [pyfiglet](https://pypi.org/project/pyfiglet/)