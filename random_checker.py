def random_checker(func, size = 1000):
    from math import pi
    green = 0
    for i in range(size * size):
        a = func(0, size) - size//2
        b = func(0, size) - size//2
        if a * a + b * b <= size * size // 4:
            green += 1
    return green / (pi * size * size // 4)
