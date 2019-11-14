from stellar_base.builder import Builder
seed = "SAUV4WPT2IY3N5OVQHGYLMOH4SPOUFS27YEER3BYFWVVIWSEETFIHTLQ"
builder = Builder(secret=seed)
# builder = Builder(secret=seed, network='public') for LIVENET

bob_address = 'GBCCC62LUXPDL7DLNQPYJWASA672CCJOLCJRBSIFXNIPRMQRRQ2HCWW6'
builder.append_payment_op(bob_address, '10', 'XLM')
builder.add_text_memo("zxc") # string length <= 28 bytes
builder.sign()

# Uses an internal horizon instance to submit over the network
builder.submit()
