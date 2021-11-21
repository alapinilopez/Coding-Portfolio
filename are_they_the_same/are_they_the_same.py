

def comp(array1, array2):
    newArray = []
    if array1 == None or array2 == None:
        return False
    for num in array1:
        squareValue = num ** 2
        newArray.append(squareValue)
    sortedSquareArray = sorted(newArray)
    sortedArray2 = sorted(array2)
    if sortedArray2 == sortedSquareArray:
        return True
    else:
        return False
#         if newArray == array2


# por cada num array:
#     elevar los valores al cuadrado y meter en newArray

#     si nuevo array es igual array 1 elevado 2
#     return True
#     else return False


a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
comp(a1, a2)
