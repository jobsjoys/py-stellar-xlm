from stellar_base.keypair import Keypair
import requests

kp = Keypair.random()

publickey = kp.address().decode()
seed = kp.seed().decode()
url = 'https://friendbot.stellar.org'
r = requests.get(url, params={'addr': publickey})
print(publickey)
print(seed)



# GBCCC62LUXPDL7DLNQPYJWASA672CCJOLCJRBSIFXNIPRMQRRQ2HCWW6
# SDXQL5ZLNBQCJPX3X45KQ7HOAFGXKFHGG6Y2URFITMELW2UEBGNCFTG6
# to
# GBZUZVZYZMXI5GC3XQCRQAZVUGLVBYY6KSWPGWZIUVPP3K3D4YLDYXQ3
# SAUV4WPT2IY3N5OVQHGYLMOH4SPOUFS27YEER3BYFWVVIWSEETFIHTLQ