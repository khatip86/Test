import pulp

# Объявление проблемы, цены кузова машины
problem = pulp.LpProblem("CarBodyDesign", pulp.LpMinimize)

# Границы кол-ва метров квадратных материала
metal = pulp.LpVariable("metal", lowBound=0, cat="Continuous")
glass = pulp.LpVariable("glass", lowBound=4, upBound=5, cat="Continuous")
plastic = pulp.LpVariable("plastic", lowBound=0, cat="Continuous")

# Цена кузова
problem += 25 * metal + 20 * glass + 40 * plastic

# Площадь и вес кузова
problem += metal + glass + plastic == 14  # Total area constraint
problem += 10 * metal + 15 * glass + 3 * plastic <= 150  # Weight constraint

# Решение проблемы, с использованием метода оптимизации линейного программирования
problem.solve()

# Вывод
print("Solution:")
print("Metal:", pulp.value(metal), "m²")
print("Glass:", pulp.value(glass), "m²")
print("Plastic:", pulp.value(plastic), "m²")
print("Total cost:", pulp.value(problem.objective), "$")
