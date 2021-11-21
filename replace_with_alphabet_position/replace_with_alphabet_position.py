alphabet = "abcdefghijklmnopqrstuvwxyz"


def alphabet_position(text):
    # guardar el text en un array
    # asignarle a cada letra su valor del alfabeto
    # poner espacio entre caracteres y devolverlo en string
    # por cada letra del string reemplazarlo por el alfabeto
    if text == str:
        text = text.lower()
        text = ""

        for c in text:
            if c.isalpha() == True:
                result = result + " " + str(alphabet.index(c) + 1)
        return result.lstrip(" ")
