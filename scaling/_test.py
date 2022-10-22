# def xor_crypt_string(data, key = 'awesomepassword', encode = False, decode = False):
#    from itertools import cycle
#    import base64


  
   
#    if decode:
#     pass

#    if encode:
#     xored = xored.encode("UTF-8")
#     xored=base64.b64encode(xored)
#     xored = xored.decode("UTF-8")
#    return xored
   


# secret_data = "XOR procedure"

# print("The cipher text is")
# print (xor_crypt_string(secret_data, encode = True))
# print("The plain text fetched")
# print (xor_crypt_string(xor_crypt_string(secret_data, encode = True), decode = True))

import os, sys


with open(os.path.join(os.path.dirname(sys.argv[0]), 'test.txt')) as file:
    text = [line.split()[::-1] for line in file.readlines()]

with open('output.txt', "w") as file:
    file.write("\n".join([" ".join(line) for line in text]))