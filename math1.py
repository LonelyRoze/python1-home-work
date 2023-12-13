import math

def fibonacci_golden_ratio(n):
    phi = (1 + math.sqrt(5)) / 2
    fibonacci_number = round((math.pow(phi, n) - math.pow(-1/phi, n)) / math.sqrt(5))
    return fibonacci_number
# здесь идет вычисление числа фиббоначи - золотое сечение
# решил вспомнить math
# пример использования
for i in range(10):
    print(f"Fibonacci({i}):", fibonacci_golden_ratio(i))

