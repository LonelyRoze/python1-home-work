from enum import Enum, auto
# автоматическое присвоение уникального значения для каждого дня недели
class Weekday(Enum):
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()
    SUNDAY = auto()

print(Weekday.MONDAY)
print(Weekday.MONDAY.value)

for day in Weekday:
    print(day)

