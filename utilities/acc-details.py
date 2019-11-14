from stellar_base.address import Address

publickey = 'GBCCC62LUXPDL7DLNQPYJWASA672CCJOLCJRBSIFXNIPRMQRRQ2HCWW6'#'GAU3DAERZWH4DC4XTUQ5IXYHJHZ67LQ5OCXU5GJJOADIPSJMGELBJAFW'
address = Address(address=publickey)  # See signature for additional args
address.get()  # Get the latest information from Horizon

balance = address.balances
print(address.balances)
if 'balance' in balance[-1]:
    print('balance: {}'.format(int(float(balance[-1]['balance']))))

last_transaction = address.transactions(order='desc', limit=1)
if 'memo' in last_transaction['_embedded']['records'][0]:
    print('memo: {}'.format(last_transaction['_embedded']['records'][0]['memo']))

last_payment = address.payments(order='desc', limit=1)
if 'amount' in last_payment['_embedded']['records'][0]:
    print('amount: {}'.format(last_payment['_embedded']['records'][0]['amount']))
if 'asset_type' in last_payment['_embedded']['records'][0]:
    print('asset_type: {}'.format(last_payment['_embedded']['records'][0]['asset_type']))
if 'asset_code' in last_payment['_embedded']['records'][0]:
    print('asset_code: {}'.format(last_payment['_embedded']['records'][0]['asset_code']))
if 'transaction_successful' in last_payment['_embedded']['records'][0]:
    print('success: {}'.format(bool(last_payment['_embedded']['records'][0]['transaction_successful'])))

if last_payment['_embedded']['records'][0]['from'] == publickey:
    print("Ignore")
else:
    print("Valid")