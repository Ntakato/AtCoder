s = input()
n = len(s)


def is_kaibun(kaibun):
    for i in range(len(kaibun)//2):
        if kaibun[i] != kaibun[-i-1]:
            return False
    return True


if(is_kaibun(s) and is_kaibun(s[:(n-1)//2]) and is_kaibun(s[(n+3)//2-1:])):
    print('Yes')
else:
    print('No')
