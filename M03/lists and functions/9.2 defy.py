def get_odds():
    for num in range(10):
        if num % 2 != 0:
            yield num
