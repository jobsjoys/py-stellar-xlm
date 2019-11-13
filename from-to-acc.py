from stellar_base.builder import Builder
seed = "SANYOBAAZ26YNCIRMMCBFX6IIDPFLNYA4WTXNTAXWE77XIG5UXMYV5CR"
builder = Builder(secret=seed)
# builder = Builder(secret=seed, network='public') for LIVENET

bob_address = 'GAU3DAERZWH4DC4XTUQ5IXYHJHZ67LQ5OCXU5GJJOADIPSJMGELBJAFW'
builder.append_payment_op(bob_address, '696', 'XLM')
builder.add_text_memo("I AM A LEGEND") # string length <= 28 bytes
builder.sign()

# Uses an internal horizon instance to submit over the network
builder.submit()
