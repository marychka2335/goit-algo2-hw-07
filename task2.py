import timeit
from functools import lru_cache
import matplotlib.pyplot as plt

class SplayTree:
    def __init__(self):
        self.tree = {}
        
    def get(self, key):
        return self.tree.get(key, None)
    
    def put(self, key, value):
        self.tree[key] = value

@lru_cache(maxsize=None)
def fibonacci_lru(n):
    if n < 2:
        return n
    return fibonacci_lru(n-1) + fibonacci_lru(n-2)

def fibonacci_splay(n, tree):
    if tree.get(n) is not None:
        return tree.get(n)
    if n < 2:
        result = n
    else:
        result = fibonacci_splay(n-1, tree) + fibonacci_splay(n-2, tree)
    tree.put(n, result)
    return result

def measure_time_lru(n):
    start_time = timeit.default_timer()
    fibonacci_lru(n)
    return timeit.default_timer() - start_time

def measure_time_splay(n, tree):
    start_time = timeit.default_timer()
    fibonacci_splay(n, tree)
    return timeit.default_timer() - start_time

if __name__ == "__main__":
    ns = list(range(0, 951, 50))
    lru_times = []
    splay_times = []
 
    for n in ns:
        lru_time = measure_time_lru(n)
        lru_times.append(lru_time)

        tree = SplayTree()
        splay_time = measure_time_splay(n, tree)
        splay_times.append(splay_time)

    # Побудова графіка
    plt.plot(ns, lru_times, label='LRU Cache')
    plt.plot(ns, splay_times, label='Splay Tree')
    plt.xlabel('n - Fibonacci Number')
    plt.ylabel('Time (s)')
    plt.title('Comparison of Fibonacci Calculation Performance')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Виведення результатів у вигляді таблиці
    print(f"{'n':<10}{'LRU Cache Time (s)':<25}{'Splay Tree Time (s)':<25}")
    print('-' * 60)
    for n, lru_time, splay_time in zip(ns, lru_times, splay_times):
        print(f"{n:<10}{lru_time:<25}{splay_time:<25}")
