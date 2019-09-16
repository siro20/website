import numpy as np
import matplotlib.pyplot as plt

x = [270, 310, 260, 275, 310, 150, 275, 360, 245, 265, 200, 100, 160, 325]
y = [38.5, 40.2, 70, 38.2, 40.3, 21.5, 39.1, 47.2, 53.0, 34.7, 36.4, 22.4, 22.9, 69]

fig, ax = plt.subplots()
fig.set_size_inches(12, 8, forward=True)
ax.set(title='Voc vs module power', xlabel='module power [W]', ylabel='open collector voltage [V]')
ax.scatter(x, y, s=30, alpha=0.75, marker='x')
fig.savefig("test.png")
plt.show()
