def duplicate_encoder(palabra):


palabra = palabra.lower()

string_vacio = ''

diccionario = dict.fromkeys(word, 0)

for char in palabra:
    if char in diccionario:
        diccionario[char] += 1
    else:
        diccionario[char] = 1

print(diccionario)

for char in palabra:
    if diccionario[char] > 1:
        string_vacio = string_vacio + ')'
    else:
        string_vacio = string_vacio + '('

print(string_vacio)
