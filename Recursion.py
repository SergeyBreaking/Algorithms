def rec_sum(n, s=0):
    x, y = divmod(n, 10)
    s += y
    if x == 0:
        return print(s)
    else:
        rec_sum(x, s)


rec_sum(int(input()))