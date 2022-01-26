x = 1
y = 2


def local_scope():
    x = 500
    y = 700
    return x, y


x, y = local_scope()
print(x, y)

a = 1

def l_scope(a):
    if a == 1:
        print('Yes')
        return 2
    else:
        return a


a = local_scope(a)