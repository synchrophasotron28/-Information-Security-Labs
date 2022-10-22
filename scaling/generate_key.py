fileText1 = "abcdefghijklmnop" #тут все содержимое текстового файла одной строкой
key1 = "12345" #введенный ключ
print(key1)


def generate_key(key='12345',fileText = "abcdefghijklmnop"):
    #вычисляем количество символов, которое необходимо добавить к ключу
    symbolsAmountToAdd = (len(fileText) - 1) - len(key)
    #дебаг
    # print(symbolsAmountToAdd)

    if symbolsAmountToAdd > 0:
        index = 0
        shift = 0
        initialKey = list(key) #здесь делаем массив из строки с изначальным ключом
        key = list() #начальный ключ делаем пустым массивом
        for i in range(len(fileText)): #для каждого индекса символа из исходного текстового файла
            #дебаг
            # print(fileText[i])
            #тут надо подумоть, так как я не помню уже, если честно, но вроде особо ничего сложного
            if i % len(initialKey) == 0 and i != 0:
                shift += 1 #прибавляем смещение
                #когда смещение равно длине ключа - обнуляем смещение
                if shift == len(initialKey):
                    shift = 0
            #вычисляем индекс, по которому будем добавлять символ в итоговый ключ
            index = (((i % len(initialKey)) + shift) % len(initialKey))
            #добавляем символ к ключу
            key.append(initialKey[index])
            index += 1 #не помню, зачем
             #дебаг и вывод длины в консоль
        return key
key = generate_key()
print(key)
print("Длина ключа: ", len(key), "\nДлина текста: ", len(fileText1))
