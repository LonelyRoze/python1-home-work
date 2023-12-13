import math
# это решение квадратного уравнения
def solve_quadratic_equation(a, b, c):
    # вычисление дискриминант
    discriminant = b**2 - 4*a*c

    # проверка значения дискриминанта
    if discriminant > 0:
        # два корня
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        # один корень
        root = -b / (2*a)
        return root
    else:
        # нет корней
        return "нет корней"


a = int(input("введите коэффициенты уравнения: "))
b = int(input())
c = int(input())

roots = solve_quadratic_equation(a, b, c)
print("корни: ", roots)
