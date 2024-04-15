import numpy as np
from matplotlib import pyplot as plt

x = np.arange(400)
y = 400 * (np.sin(0.5*np.pi*5*(x/200)))
plt.plot(x, y)
plt.show()
