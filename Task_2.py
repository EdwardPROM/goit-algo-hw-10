import random
import scipy.integrate as spi

# Визначення функції
def f(x):
    return x ** 2

def monte_carlo_integration(func, a, b, experiments=10000):
    sum_of_samples = 0.0
    
    for _ in range(experiments):
        x = random.uniform(a, b)
        sum_of_samples += func(x)
    
    average_value = sum_of_samples / experiments
    
    return average_value * (b - a)


a = 0
b = 2
print(f"Оцінка значення інтеграла методом Монте-Карло: {monte_carlo_integration(f, a, b)}")

result, error = spi.quad(f, a, b)
print(f"За допомогою функції quad: {result}")
