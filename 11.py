import numpy as np
import matplotlib.pyplot as plt

# Задаємо функцію
def f(x):
    return np.sin(4 * x)

# Дані для xi
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8]) / 10.0
y = f(x)

# Лінійна апроксимація (пряма)
coeffs_line = np.polyfit(x, y, 1)
y_line_approx = np.polyval(coeffs_line, x)

# Параболічна апроксимація
coeffs_parabola = np.polyfit(x, y, 2)
y_parabola_approx = np.polyval(coeffs_parabola, x)

# Побудова графіків
plt.scatter(x, y, color='red', label='Задані точки')
plt.plot(x, y_line_approx, label='Лінійна апроксимація (пряма)', color='green')
plt.plot(x, y_parabola_approx, label='Параболічна апроксимація', color='blue')

plt.title('МНК апроксимація функції f(x) = sin(4x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
