class Money:
    '''Stores money as pennies, uses integer arithmetic'''
    def __init__(self, amount):
        assert isinstance(amount, int)
        self.amount = amount

    def __str__(self):
        sign = '-' if self.amount < 0 else ''
        amount = abs(self.amount)

        dollars = amount // 100
        cents = amount % 100

        return f"{sign}${dollars}.{str(cents).zfill(2)}"

    def __add__(self, other):
        if isinstance(other, int):
            other = Money(other)
        return Money(self.amount + other.amount)
    
    __radd__ = __add__


if __name__ == "__main__":
    m1 = Money(345)
    m2 = Money(4589)
    m3 = Money(100)
    print(m1,m2,m3)
    print(m1 +m2)
    print(m3 + 899)
    print()