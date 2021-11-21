

def duplicate_encode(word):

    word = word.lower()
    encoded_word = ""

    for c in word:
        if word.count(c) > 1:
            encoded_word += ")"
        else:
            encoded_word += "("
    return(encoded_word)
