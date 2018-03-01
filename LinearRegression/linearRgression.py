import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pods

data = pods.datasets.olympic_marathon_men()
X = data["X"]
Y = data["Y"]
m = 0
c = 0
alpha = 0.01


def linear(X, Y, m, c):
    for j in range(100):
        C = -(Y - m * X).sum()
        M = -((Y - m * X) * X).sum()
        c = c + alpha * C
        m = m + alpha * M
    return m, c

a, b = linear(X, Y, m, c)
Y_pre = a * X + b
plt.plot(X, Y, 'rx')
plt.plot(X, Y_pre, 'b')
plt.show()

# print(X)
