import matplotlib.pyplot as plt

a = 3.45
b = 0.76

x = [0, 1, 2, 3, 4, 5, 6]

y = []

for xn in x:

    yn = round((a + (xn * b)), 2)

    y.append(yn)

print(y)

plt.plot(x, y)
plt.title('title name')
plt.xlabel('x_axis name')
plt.ylabel('y_axis name')
plt.show()
