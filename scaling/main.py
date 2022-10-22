'''
Гаммирование -  метод симметричного шифрования, заключающийся в «наложении» последовательности,
состоящей из случайных чисел, на открытый текст.

Алгоритм шифрования и дешифрования XOR преобразует простой текст
в формат байтов ASCII и использует процедуру XOR для преобразования
его в указанный байт.
'''
import base64
import os
import sys
from generate_key import generate_key

# def xor_transformation(input_file, output_file, key='12345'):
#     with open(output_file, "w") as f_xor:
#         with open(input_file, "r") as f:
#             for line in f:
#                 xored = ""
#                 xored += ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(line, cycle(key)))
#             f_xor.write(xored)

def xor_transformation(filein:str, fileout:str, key='12345', base64enc=False, base64dec=False):
    '''
    делает xor из файла filein со строкой key и записывает в файл fileout
    '''
    with open(os.path.join(os.path.dirname(sys.argv[0]), filein), encoding="UTF-8") as file:
        with open(os.path.dirname(sys.argv[0])+'/'+fileout, "w", encoding="UTF-8") as file_xor:
            line = file.read()
            # Декодирует строку из base64
            if base64dec:
                line = base64.b64decode(line.encode("UTF-8")).decode("UTF-8")
            xored = ""
            
            xored += ''.join((chr(ord(x) ^ ord(y)) for (x,y) in zip(line, generate_key(key=key, fileText=line))))
            # Кодирует строку в base64
            if base64enc:
                xored = base64.b64encode(xored.encode("UTF-8")).decode("UTF-8")
            file_xor.write("".join(xored))
xor_transformation('test2.txt', 'output.txt', base64enc=True)
xor_transformation('output.txt', 'output2.txt', base64dec=True)

# xor_transformation('test2.txt', 'output.txt')
# xor_transformation('output.txt', 'output2.txt')
