import sys
import io

WATER_PER_KG = 30
ML_IN_L = 1000

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("Вас приветсвует консольный фитнес-бот!")
user_name = input("Введите ваше имя: ")

try:
    user_age = int(input("Введите ваш возраст: "))
except ValueError:
    print("Пожалуйста, введите в числовом формате сколько вам полных лет.")
    sys.exit("Программа завершена из-за ошибки")

try:
    user_weight = float(input("Введите ваш вес: "))
except ValueError:
    print("Пожалуйста, введите вес в числовом формате. Например, 50.1 или 50.")
    sys.exit("Программа завершена из-за ошибки")

try:
    user_height = float(input("Введите ваш рост в метрах: "))
except ValueError:
    print("Пожалуйста, введите рост в числовом формате в метрах.", end=" ")
    print("Например, 1.78 или 2 .")
    sys.exit("Программа завершена из-за ошибки")

# расчёт индекса массы тела
bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)

# расчёт нормы воды
water_ml = user_weight * WATER_PER_KG
water_l = water_ml / ML_IN_L

print()
print(f"Отчет для пользователя: {user_name} ({user_age} г.)")
print(f"Твой индекс массы тела (ИМТ): {bmi}")
print(f"Рекомендуемая норма воды: {water_l: .1f} л. в день", end="\n" * 2)
print("Расчёт окончен. Будьте здоровы!")
