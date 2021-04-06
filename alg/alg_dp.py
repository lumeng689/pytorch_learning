def cut_rod1(p, n):
    if n == 0:
        return 0

    q = -1

    for i in range(1, n + 1):
        q = max(q, p[i] + cut_rod1(p, n - i))

    return q


def bottom_up_cut_rod(p, n):
    r = [0 for _ in range(n + 1)]
    s = [0 for _ in range(n + 1)]

    for j in range(1, n + 1):
        q = -1
        for i in range(1, j + 1):
            if q < p[i] + r[j - i]:
                q = p[i] + r[j - i]
                s[j] = i
        r[j] = q

    return r, s


def test1():
    p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

    # r = cut_rod1(p, 10)
    # print("r=", r)
    r, s = bottom_up_cut_rod(p, 10)
    print("r=", r)
    print("s=", s)


if __name__ == '__main__':
    test1()
    # test2()
