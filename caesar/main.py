'''
Шифр Цезаря

На вход подается к-целое число
Закодировать число со сдвигом на к
'''

import os
import sys

NUMBERS = ' 1234567890'
ALFAVTT_EN =  'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ALFAVIT_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
ALFAVIT = NUMBERS+ALFAVIT_RU+ALFAVTT_EN
ALFAVIT = ALFAVIT.lower()
def caesar(num, shift):
    '''
    функция, реализующая шифр Цезаря
    На вход подается к-целое число
    Закодировать число со сдвигом на к
    '''
    res = ''
    if num:
        num = num.lower()
        for i in num:
            if i in ALFAVIT:
                position=ALFAVIT.find(i)
                nextposition = (position + shift)%len(ALFAVIT)
                res += ALFAVIT[nextposition]
            else:
                res += i
    return res

def caesar_file(filein:str, fileout:str, shift):
    '''
    функция для чтения и записи
    '''
    with open(os.path.join(os.path.dirname(sys.argv[0]), filein), encoding="UTF-8") as file:
        with open(os.path.dirname(sys.argv[0])+'/'+fileout, "w", encoding="UTF-8") as file_csr:
            line = file.readline(500)
            while line:
                file_csr.write("".join(caesar(line, shift)))
                line = file.readline(500)
# print(caesar('890123457ф', 1))
# print(caesar('890abcz абвя', 1))
caesar_file('test.txt', 'output.txt', shift=1)
caesar_file('output.txt', 'output2.txt', shift=-1)
