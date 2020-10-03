def maskify(cc):
    str = ''
    for char in cc[:-4]:
        str += '#'
    str += cc[-4:]

    return str

def maskify1(cc):
    return "#"*(len(cc)-4) + cc[-4:]

def maskify2(cc):
    l = len(cc)
    if l <= 4: return cc
    return (l - 4) * '#' + cc[-4:]

print(maskify('123456789'))
print(maskify1('987654321'))
print(maskify2('159623847'))