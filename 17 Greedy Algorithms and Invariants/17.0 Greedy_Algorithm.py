def change_making(cents):
    COINS = [1, 5, 10, 25, 50, 100]

    COINS.sort()
    COINS.reverse()

    num_coins = 0
    for coin in COINS:
        num_coins += cents // coin
        cents %= coin
    return num_coins




