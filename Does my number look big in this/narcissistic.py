def narcissistc(value):
    # convertir value en un str para sacarle el len y elevar cada digito por su len
    # sumar cada digito elevado
    str_value = str(value)
    len_value = len(str_value)
    total_sum = 0
    for i in str_value:
        total_sum += int(i) ** len_value
    return total_sum == int(str_value)


if __name__ == "__main__":
    assert narcissistc(7) == True
    assert narcissistc(371) == True
