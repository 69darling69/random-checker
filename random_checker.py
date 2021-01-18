def random_checker(func, size = 1000):
    from math import pi
    from concurrent.futures import ThreadPoolExecutor
    from os import cpu_count
    sum = 0
    cores = cpu_count()
    threads_list = list()
    with ThreadPoolExecutor() as executor:
        for _ in range(cores):
            threads_list.append(executor.submit(increaser, func, size, size*size//cores))
    for thread in threads_list:
        print(thread.result())
        sum += thread.result()
    return sum / (pi * size * size // 4)

def increaser(func, size, times):
    sum = 0
    for _ in range(times):
        a = func(0, size) - size//2
        b = func(0, size) - size//2
        if a * a + b * b <= size * size // 4:
            sum += 1
    return sum
