def divisible_count(x, y, k):
    # encontrar nums divisibles por K entre X e Y.
    counter = 0

    for num in range(x, y):
        if num % k == 0:
            counter = counter + 1

    return counter


if __name__ == "__main__":
    assert divisible_count(6, 11, 2) == 3
