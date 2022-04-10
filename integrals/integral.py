#matplotlib inline
import matplotlib               # импорт библиотек
import matplotlib.pyplot as plt
import numpy as np
import random

n = 5                  # Установка количества разбиений (n > 0)
type_of_furnishing = 0 # Тип оснащения (0 - левые, 1 - правые, 2 - средние, 3 - случайные точки)

upper = 2       # Верхняя граница интеграла
lower = 1       # Нижняя граница интеграла
def fun(x):     # Исследуемая подынтегральная функция
    return x**2 
value_of_integral = 7/3 # Точное значение интеграла

x = np.linspace(lower-0.2,upper+0.2,100) # точки для графика функции
y = fun(x)

fraction = np.linspace(lower,upper,n+1)  # точки отрезков

if type_of_furnishing == 0:
    furnishing = np.arange(lower,upper,(upper-lower)/n)
if type_of_furnishing == 1:
    furnishing = np.arange(upper,lower,-(upper-lower)/n)[::-1]
if type_of_furnishing == 2:
    furnishing = np.arange(lower+(upper-lower)/(2*n),upper,(upper-lower)/n)
if type_of_furnishing == 3:
    furnishing = np.zeros(n)
    for i in range(n):
        furnishing[i] = fraction[i]+(upper-lower)/n*random.random()
furnishing = fun(furnishing)             # точки оснащения

# Подсчет сравнение и вывод интегральной суммы
integral_sum = 0                
for i in range(n):
    integral_sum += furnishing[i]*(upper-lower)/n
print(f"sum: {integral_sum}")
print(f"delta: {abs(integral_sum-value_of_integral)}")

# График функции и прямоугольники
plt.figure(figsize=(12, 8), dpi=80) 
plt.title("y = x^2")                
plt.xlabel("x")
plt.ylabel("y") 
plt.grid()      
plt.plot(x, y)
plt.plot([lower-0.2,upper+0.2], [0,0])
for i in range(n):
    # левый отрезок
    plt.plot([fraction[i],fraction[i]], [0, furnishing[i]], linewidth=1, color='red') 
    # правый отрезок
    plt.plot([fraction[i+1], fraction[i+1]], [0, furnishing[i]], linewidth=1, color='red') 
    # перекладина
    plt.plot([fraction[i], fraction[i+1]], [furnishing[i],furnishing[i]], linewidth=1, color='red') 

# Вычисление интегральной суммы через метод трапеций
furnishing_trapezoid = fun(fraction)
integral_sum = 0
for i in range(n):
    integral_sum += (furnishing_trapezoid[i]+furnishing_trapezoid[i+1])*(upper-lower)/n/2
print(f"sum: {integral_sum}")

# График функции и трапеций
plt.figure(figsize=(12, 8), dpi=80)
plt.title("y = x^2") 
plt.xlabel("x") 
plt.ylabel("y")
plt.grid()     
plt.plot(x, y)  
plt.plot([lower-0.2,upper+0.2], [0,0]) # ось OX
for i in range(n):
    # левый отрезок
    plt.plot([fraction[i],fraction[i]], [0, furnishing_trapezoid[i]], linewidth=1, color='red') 
    # правый отрезок
    plt.plot([fraction[i+1], fraction[i+1]], [0, furnishing_trapezoid[i+1]], linewidth=1, color='red') 
    # перекладина
    plt.plot([fraction[i], fraction[i+1]], [furnishing_trapezoid[i],furnishing_trapezoid[i+1]], linewidth=1, color='red') 
