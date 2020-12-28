# fraction.py

def frac2dec(num,den=1):
    return num if den == 0 else num/den

print(frac2dec(3))      # 3.0
print(frac2dec(3,2))    # 1.5
