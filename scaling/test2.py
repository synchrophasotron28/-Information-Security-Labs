import base64

# Создайте строку
s = "Hello World!"

# Кодирование строки в байты
b = s.encode("UTF-8")
#b'Hello World!'

# Base64 кодирование в байты
e = base64.b64encode(b)
#b'SGVsbG8gV29ybGQh'

# Декодирование байтов Base64 в строку
s1 = e.decode("UTF-8")
# Печать строки в кодировке Base64
#Base64 Encoded: SGVsbG8gV29ybGQh
print("Base64 Encoded:", s1)

# Кодирование строки в кодировке Base64 в байты
b1 = s1.encode("UTF-8")
#b'SGVsbG8gV29ybGQh'


# Декодирование байтов Base64
d = base64.b64decode(b1)
#b'Hello World!'


# Декодирование байтов в строку
s2 = d.decode("UTF-8")
#Hello World!
