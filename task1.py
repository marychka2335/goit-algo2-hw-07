import random
from timeit import default_timer as timer
from functools import lru_cache

# Параметри задачі
K = 1000
N_len = 100000
Q_len = 50000

# Функція для обчислення суми елементів на відрізку від L до R включно без кешу
def range_sum_no_cache(array, L, R):
    return sum(array[L:R+1])

# Функція для оновлення значення елемента масиву за індексом без кешу
def update_no_cache(array, index, value):
    array[index] = value

# LRU-кеш розміром 1000 для функції range_sum_with_cache
@lru_cache(maxsize=1000)
def range_sum_with_cache(array, L, R, cache_ver):
    return sum(array[L:R+1])

# Функція для оновлення значення елемента масиву за індексом з кешем
def update_with_cache(array, index, value):
    array[index] = value
    range_sum_with_cache.cache_clear()

if __name__ == '__main__':
    # Ініціалізація масиву
    array = [random.randint(1, 100) for _ in range(N_len)]

    # Генерація запитів
    queries = []
    for _ in range(Q_len):
        if random.choice(['Range', 'Update']) == 'Range':
            L = random.randint(0, N_len-1)
            R = random.randint(L, N_len-1)
            queries.append(('Range', L, R))
        else:
            index = random.randint(0, N_len-1)
            value = random.randint(1, 100)
            queries.append(('Update', index, value))

    # Виконання запитів без використання кешу
    start_time = timer()
    for query in queries:
        if query[0] == 'Range':
            range_sum_no_cache(array, query[1], query[2])
        else:
            update_no_cache(array, query[1], query[2])
    no_cache_duration = timer() - start_time

    # Виконання запитів з використанням LRU-кешу
    cache_ver = 1
    start_time = timer()
    for query in queries:
        if query[0] == 'Range':
            range_sum_with_cache(tuple(array), query[1], query[2], cache_ver)
        else:
            update_with_cache(array, query[1], query[2])
            cache_ver += 1
    with_cache_duration = timer() - start_time

    # Виведення результатів
    print(f"Час виконання без кешування: {no_cache_duration:.2f} секунд")
    print(f"Час виконання з LRU-кешем: {with_cache_duration:.2f} секунд")
