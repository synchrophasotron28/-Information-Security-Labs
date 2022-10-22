from email import base64mime
from itertools import cycle
import base64

data = "XOR procedure"
key = 'awesomepassword'

xored = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(data, cycle(key)))
print("1",xored)
xored = xored.encode("UTF-8")
xored=base64.b64encode(xored)
xored = xored.decode("UTF-8")
print("2",xored)

xored = xored.encode("UTF-8")
xored = base64.b64decode(xored)
xored = xored.decode("UTF-8")
print("3",xored)