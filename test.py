import numpy as np
import matplotlib.pyplot as plt
from MF import *

x = np.arange(0, 100, 0.5)
m = np.arange(0, 10, 0.05)
Y = [np.array([mfTisVB(z) for z in m]),
     np.array([mfTisB(z) for z in m]),
     np.array([mfTisN(z) for z in m]),
     np.array([mfTisS(z) for z in m])]
Z = [np.array([mfDistisL(z) for z in x]),
     np.array([mfDistisA(z) for z in x]),
     np.array([mfDistisSh(z) for z in x])]
M = [np.array([mfPisVH(z) for z in x]),
     np.array([mfPisH(z) for z in x]),
     np.array([mfPisF(z) for z in x]),
     np.array([mfPisLow(z) for z in x])]

plt.figure(figsize = (10,10))
ax = []
ax.append(plt.subplot(2,2,1))
for y in Y:
    plt.plot(m, y, linewidth = 3)
ax.append(plt.subplot(2,2,2))
for y in Z:
    plt.plot(x, y, linewidth = 3)
ax.append(plt.subplot(2, 2, 3))
for y in M:
    plt.plot(x, y, linewidth = 3)
plt.show()
