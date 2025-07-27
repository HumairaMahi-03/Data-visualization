import matplotlib.pyplot as plt
import numpy as np

x = np.arange(11)


y1=x+2
y2=x+3
plt.plot(x, y1,linewidth=2, color='blue',label='x+2')
plt.plot(x, y2,linewidth=2, color='orange',label='x+3')
plt.legend(loc='lower right')
plt.show()
