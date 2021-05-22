i, dan = 0, 0

for dan in range(2, 10, 1):
    for i in range(1, 10, 1):
        print("%d X %d = %2d" % (dan, i, dan*i))
    print("----------")
