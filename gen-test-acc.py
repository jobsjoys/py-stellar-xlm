from stellar_base.keypair import Keypair
import requests

kp = Keypair.random()

publickey = kp.address().decode()
seed = kp.seed().decode()
url = 'https://friendbot.stellar.org'
r = requests.get(url, params={'addr': publickey})
print(publickey)
print(seed)



# GAGIRMMBMT6SERBT7UR3NXS5LS2JWMFNYFVR3VROX2M4RB2NGZMIQYHS
# SDEYJDC2TP6T7LMF5E2GVEYWHNNM3BFLRLU2HPMXVXHOCWQQVBYFUXBG
# to
# GAU3DAERZWH4DC4XTUQ5IXYHJHZ67LQ5OCXU5GJJOADIPSJMGELBJAFW