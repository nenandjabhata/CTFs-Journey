from Crypto.Util.number import *

e =  1
c =  9327565722767258308650643213344542404592011161659991421
n =  245841236512478852752909734912575581815967630033049838269083

p = 416064700201658306196320137931
q = 590872612825179551336102196593
phi = (p - 1 ) * (q - 1)
d = inverse(e, phi)
m = pow(c, d, n)
var =hex(m)[2:]
decoded = bytes.fromhex(var).decode('utf-8')
print(decoded)

