def counter(start=0):
    def step():
        nonlocal start # для использования start из counter()
        start += 1
        return start

    return step


c1 = counter(10)
c2 = counter()

print(c1(), c2())