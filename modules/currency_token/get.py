def get(currency_module):
    details = currency_module.get()
    return {"name": details.name, "symbol": details.symbol, "decimals": details.decimals}
