# Завдання 1

import timeit


def find_coins_greedy(amount: int):
    result = {}
    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount = amount % coin
    return result


def find_min_coins(amount: int):
    min_coins_required = [0] + [float("inf")] * amount
    last_coin_used = [0] * (amount + 1)
    for s in range(1, amount + 1):
        for coin in coins:
            if s >= coin and min_coins_required[s - coin] + 1 < min_coins_required[s]:
                min_coins_required[s] = min_coins_required[s - coin] + 1
                last_coin_used[s] = coin
    result = {}
    current_sum = amount
    while current_sum > 0:
        coin = last_coin_used[current_sum]
        result[coin] = result.get(coin, 0) + 1
        current_sum = current_sum - coin
    return result


if __name__ == "__main__":
    coins = [50, 25, 10, 5, 2, 1]
    amount = 113
    # Результати виконання функцій
    print(f"Coins: {coins}")
    print(f"Amount: {amount}")
    print(f"Greedy algorithm: {find_coins_greedy(amount)}")
    print(f"Dynamic programming: {find_min_coins(amount)}")

    # Порівняння швидкості виконання функцій при різних значеннях amount
    print("\nПорівняння швидкості виконання функцій при різних значеннях amount:")
    greedy_algorithm_result = {}
    g_amount = amount
    for i in range(1, 6):
        greedy_algorithm_time = timeit.timeit(
            lambda: find_coins_greedy(g_amount), number=50)
        greedy_algorithm_result[g_amount] = greedy_algorithm_time
        g_amount *= 5
    print(f"Greedy algorithm result (amount: time): {greedy_algorithm_result}")

    dynamic_programming_result = {}
    dp_amount = amount
    for i in range(1, 6):
        dynamic_programming_time = timeit.timeit(
            lambda: find_min_coins(dp_amount), number=50)
        dynamic_programming_result[dp_amount] = dynamic_programming_time
        dp_amount *= 5
    print(
        f"Dynamic programming result (amount: time): {dynamic_programming_result}")

    # Виводимо результати
    print("Таблиця результатів:")
    print(f"| {'-'*15:^15} | {'-'*25:^25} | {'-'*25:^25} | {'-'*25:^25} |")
    print(f"| {'Amount':^15} | {'Greedy algorithm time':^25} | {'Dynamic programming time':^25} | {'Increase coefficient':^25} |")
    print(f"| {'-'*15:^15} | {'-'*25:^25} | {'-'*25:^25} | {'-'*25:^25} |")
    for (amount1, time1), (amount2, time2) in zip(greedy_algorithm_result.items(), dynamic_programming_result.items()):
        print(
            f"| {amount1:^15} | {time1:^25.10f} | {time2:^25.10f} | {time2 / time1:^25.2f} |")
    print(f"| {'-'*15:^15} | {'-'*25:^25} | {'-'*25:^25} | {'-'*25:^25} |")

    # Висновок
    print(f'''Висновок:
          З результатів виконання програми видно, що жадібний алгоритм є набагато ефективнішим за алгоритм динамічного програмування.
          При збільшенні суми, час виконання жадібного алгоритму майже не змінюється, а час виконання алгоритму динамічного програмування збільшується у рази, 
          майже завжди кратно значенню збільшення Amount.''')
