# Decibinary

def db(x):
    temp = x
    dec = 0
    i = 0
    while temp:
        digit = temp%10
        dec += digit*(2**i)
        i += 1
        temp //= 10
    return dec

j=0
for i in range(10):
    print(' '.join(map(str, ['{:2}'.format(' ') for _ in range(j)]+['{:2}'.format(str(db(x))) for x in range(i*10,(i+1)*10)])))
    j+=2

j=4
for i in range(10, 20):
    print(' '.join(map(str, ['{:2}'.format(' ') for _ in range(j)]+['{:2}'.format(str(db(x))) for x in range(i*10,(i+1)*10)])))
    j+=2

j=8
for i in range(20, 30):
    print(' '.join(map(str, ['{:2}'.format(' ') for _ in range(j)]+['{:2}'.format(str(db(x))) for x in range(i*10,(i+1)*10)])))
    j+=2

j=12
for i in range(30, 40):
    print(' '.join(map(str, ['{:2}'.format(' ') for _ in range(j)]+['{:2}'.format(str(db(x))) for x in range(i*10,(i+1)*10)])))
    j+=2

j=16
for i in range(40, 50):
    print(' '.join(map(str, ['{:2}'.format(' ') for _ in range(j)]+['{:2}'.format(str(db(x))) for x in range(i*10,(i+1)*10)])))
    j+=2

# j=2
# for i in range(80, 90):
#     print(' '.join(map(str, ['{:2}'.format(' ') for _ in range(j)]+['{:2}'.format(str(db(x))) for x in range(i*10,(i+1)*10)])))
#     j+=2

# j=4
# for i in range(90, 100):
#     print(' '.join(map(str, ['{:2}'.format(' ') for _ in range(j)]+['{:2}'.format(str(db(x))) for x in range(i*10,(i+1)*10)])))
#     j+=2

j=8
for i in range(100, 110):
    print(' '.join(map(str, ['{:2}'.format(' ') for _ in range(j)]+['{:2}'.format(str(db(x))) for x in range(i*10,(i+1)*10)])))
    j+=2

j=8
for i in range(200, 210):
    print(' '.join(map(str, ['{:2}'.format(' ') for _ in range(j)]+['{:2}'.format(str(db(x))) for x in range(i*10,(i+1)*10)])))
    j+=2

j=8
for i in range(1000, 1010):
    print(' '.join(map(str, ['{:2}'.format(' ') for _ in range(j)]+['{:2}'.format(str(db(x))) for x in range(i*10,(i+1)*10)])))
    j+=2

# 2^3 2^2 2^1 2^0
# 1   0   1   0
# 1   0   0   2
# 0   2   1   0
#     2   0   2
#     1   3   0
#     1   2   2
#     1   1   4
#     1   0   6
#         5   0
#         4   2  
#         3   4
#         2   6
#         1   8
