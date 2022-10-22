'''
Гаммирование -  метод симметричного шифрования, заключающийся в «наложении» последовательности, 
состоящей из случайных чисел, на открытый текст.

Алгоритм шифрования и дешифрования XOR преобразует простой текст 
в формат байтов ASCII и использует процедуру XOR для преобразования 
его в указанный байт. Он предлагает следующие преимущества для своих пользователей
'''
import os, sys
from itertools import cycle
from itertools import cycle
import base64

# def xor_transformation(input_file, output_file, key='12345'):
#     with open(output_file, "w") as f_xor:
#         with open(input_file, "r") as f:
#             for line in f:
#                 xored = ""
#                 xored += ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(line, cycle(key)))
#             f_xor.write(xored)

def xor_transformation(encode=False, decode=False, key='12345'):
    if encode:
        with open(os.path.join(os.path.dirname(sys.argv[0]), 'test.txt')) as file:
            for line in file.readlines():
                    xored = ""
                    xored += '\n'.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(line, cycle(key))) 
                    # xored = xored.encode("UTF-8")
                    # xored=base64.b64encode(xored)
                    # xored = xored.decode("UTF-8") 
                
        with open(os.path.join(os.path.dirname(sys.argv[0])), 'output.txt', "w") as file_xor:
            file_xor.write("".join(["".join(line) for line in xored]))
    # if decode:
    #     # with open(os.path.join(os.path.dirname(sys.argv[0]),'output.txt')) as file:
    #     with open(os.path.dirname(sys.argv[0])+'/output.txt') as file_xor:
    #         for line in file_xor.readlines():
    #                 xored = ""
    #                 xored += '\n'.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(line, cycle(key))) 
    #                 print(xored)
    #                 xored = xored.encode("UTF-8")
    #                 xored=base64.b64encode(xored)
    #                 xored = xored.decode("UTF-8") 

                
        # with open('output1.txt', "w") as file_xor1:
        #     file_xor1.write("".join(["".join(line) for line in xored]))
xor_transformation(encode=True)
# xor_transformation(decode=False)
