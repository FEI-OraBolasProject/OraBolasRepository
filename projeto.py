#Three lines to make our compiler able to draw:
import sys
import matplotlib
import tkinter
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 6])

plt.plot([2,3], [2,3])
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()