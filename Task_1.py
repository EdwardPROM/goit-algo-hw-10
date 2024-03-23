from pulp import *

model = LpProblem("Production_Optimization", LpMaximize)

lemonade = LpVariable("Lemonade_units", lowBound=0, cat='Integer')
fruit_juice = LpVariable("Fruit_Juice_units", lowBound=0, cat='Integer')

# Обмеження ресурсів
water_constraint = 2 * lemonade + fruit_juice <= 100 #Вода
sugar_constraint = lemonade <= 50 #Цукор
lemon_juice_constraint = lemonade <= 30 #Лимонний сік
fruit_puree_constraint = 2 * fruit_juice <= 40 #Фруктове пюре

# Додавання обмежень до моделі
model += water_constraint
model += sugar_constraint
model += lemon_juice_constraint
model += fruit_puree_constraint

# Функція максимізації
model += lemonade + fruit_juice

model.solve()

print("Результат оптимізації виробництва:")
print(f"Кількість одиниць Лимонаду: {lemonade.varValue}")
print(f"Кількість одиниць Фруктового соку: {fruit_juice.varValue}")
print(f"Загальна кількість вироблених продуктів: {value(model.objective)}")