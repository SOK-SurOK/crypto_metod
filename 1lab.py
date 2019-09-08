alfa = 'abcdefghklmnoprstw~'
N = len(alfa)


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def mult_obr(x):
    g, x, y = egcd(x, N)
    if g != 1:
        raise Exception('мультпликативно обратного не существует')
    else:
        return x % N


def zesar_get_ab_i(c1, t1, c2, t2):
    a_i = (((t1 - t2) % N) * mult_obr((c1 - c2))) % N
    b_i = (t1 + ((-(a_i * c1)) % N)) % N
    return a_i, b_i


def zesar_get_t(c, a_i, b_i):
    return ((a_i * c) % N + b_i) % N


def zesar_rashifr(cc, a_i, b_i):
    tt = ''
    for c in cc:
        if c == ' ':
            tt += c
        else:
            c = alfa.index(c)
            tt += (alfa[zesar_get_t(c, a_i, b_i)])
    return tt


def zesar(cc, c1, t1, c2, t2):
    a_i, b_i = zesar_get_ab_i(alfa.index(c1), alfa.index(t1), alfa.index(c2), alfa.index(t2))
    return zesar_rashifr(cc, a_i, b_i)


def main():
    print(zesar('lassf bfnst', 's', 'l', 'f', 'o'))


if __name__ == "__main__":
    main()
