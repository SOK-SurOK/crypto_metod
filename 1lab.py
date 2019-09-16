from tqdm import tqdm

# alfa = 'abcdefghklmnoprstw~'
alfa = 'abcdefghijklmnopqrstuvwxyz'
N = len(alfa)
NN = N*N

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def mult_obr(x, n):
    x_past = x
    g, x, y = egcd(x, n)
    if g != 1:
        raise Exception('мультпликативно обратного к ' + str(x_past) + ' по ' + str(n) + ' не существует')
    else:
        return x % n


def afin_get_ab_i(c1, t1, c2, t2, n):
    a_i = (((t1 - t2) % n) * mult_obr((c1 - c2) % n, n)) % n
    b_i = (t1 + ((-(a_i * c1)) % n)) % n

    # print('t1 t2 c1 c2')
    # print(str(t1) + ' ' + str(t2) + ' ' + str(c1) + ' ' + str(c2))
    # print('a_i b_i')
    # print(str(a_i) + ' ' + str(b_i))

    return a_i, b_i


def afin_get_t(c, a_i, b_i):
    return ((a_i * c) % N + b_i) % N


def afin_rashifr(cc, a_i, b_i):
    tt = ''
    for c in cc:
        if alfa.find(c) == -1:
            tt += c
        else:
            c = alfa.index(c)
            tt += (alfa[afin_get_t(c, a_i, b_i)])
    return tt


def zesar(cc, cc1, tt1, cc2, tt2):
    a_i, b_i = afin_get_ab_i(alfa.index(cc1), alfa.index(tt1), alfa.index(cc2), alfa.index(tt2), N)
    return afin_rashifr(cc, a_i, b_i)


def d1(a1, a2):
    a = a2 + a1*N
    a = a % NN
    # print('переменная ', a)
    return a


def double_zesar(cc, cc11, cc12, tt11, tt12, cc21, cc22, tt21, tt22):
    d1(alfa.index(cc11), alfa.index(cc12)),
    d1(alfa.index(tt11), alfa.index(tt12))
    d1(alfa.index(cc21), alfa.index(cc22))
    d1(alfa.index(tt21), alfa.index(tt22))


def double_afin_rashifr(cc1, cc2, a_i, b_i):

    tt = ((a_i * d1(alfa.index(cc1), alfa.index(cc2))) % NN + b_i) % NN
    print(tt)
    t1 = alfa[tt // N]
    t2 = alfa[tt % N]
    return t1+t2


# def file_o(name):
#     with open(name, 'r') as sf:
#         content = sf.readlines()
#         # print(content)
#     return content
#
#
# def file_wr(name, tt):
#     with open(name, 'w') as sf:
#         sf.writelines(tt)
# def rand(vxod, must):
#     kol = 0
#     try_kol = 0
#     for c1 in tqdm(alfa):
#         for c2 in alfa:
#             for t1 in alfa:
#                 for t2 in alfa:
#                     z = None
#                     kol += 1
#                     try:
#                         z = zesar(vxod, c1, t1, c2, t2)
#                     except Exception:
#                         try_kol += 1
#                     if z == must:
#                         print('t1 t2 c1 c2')
#                         print(str(t1) + ' ' + str(t2) + ' ' + str(c1) + ' ' + str(c2))
#     print()
#     print(kol)
#     print(try_kol)


def main():
    # rand('cwcugun', 'evening')
    # print(zesar(file_o('1lab_f/Cry-Substitution-13.txt')[0], 'c', 'c', 'l', 'z'))
    # print(double_zesar('ys', 'q', 'w', 'e', 't',  'y', 'u', 'i', 'n'))
    # file_o('1lab_f/Cry-Substitution-13.txt')
    # file_wr('l1.txt', file_o('Cry-Substitution-13.txt'))
    # d1(alfa.index('q'), alfa.index('y'))
    print(double_afin_rashifr('k', 'u', 601, 525))
    # alfa.index('')
    # print(mult_obr(103, 338))


if __name__ == "__main__":
    main()
