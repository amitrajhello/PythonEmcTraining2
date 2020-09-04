# variable length argument parameter
def compute(a, b, c):
    print(a + b + c)


items = [11, 22, 33, 44]
compute(items[0], items[1], items[2])
print(items[:3])
compute(*items[:3])
