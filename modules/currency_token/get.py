from typing import Dict

# Simple helper function to fetch the NFT details.
def get(currency_module) -> Dict:
    """
    This helper function is used to get the details of the currency.
    """
    details = currency_module.get()
    return {"name": details.name, "symbol": details.symbol, "decimals": details.decimals}
