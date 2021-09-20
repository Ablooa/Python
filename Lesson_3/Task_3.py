def my_func(a, b, c):
    if (a + b) > (b + c):
        if (a + b) > (c + a):
            return a + b
        else:
            return c + a
    else:
        if (b + c) > (c + a):
            return b + c
        else:
            return c + a

my_func(4, 6, 3)
