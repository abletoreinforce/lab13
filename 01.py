def Fib(n):
        if 0 <= n <= 1:
            return n
        elif n > 1:
            return Fib(n-1) + Fib(n-2)
        else:
            return None

try:
    print(Fib(int(input())))
except ValueError:
    print('Негодяй, пиши цифры')