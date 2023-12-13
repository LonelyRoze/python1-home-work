from enum import Enum
# простое перечисление цветов почти как в документации
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED)
print(Color.RED.name)
print(Color.RED.value)

for color in Color:
    print(color)

