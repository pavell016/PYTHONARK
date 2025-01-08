import numpy as np
import matplotlib.pyplot as plt
# xarr = np.array([1,7,5,4,5])
# yarr = np.array([5,2,6,4,5])

# plt.plot(xarr,yarr)
# plt.show()

x = np.array([50,20,30,10,500])
y = np.array([5,200,3,10,50])
plt.plot(x, marker = '.',
         ms=20,
         mfc='yellow',
         mec='yellow')
plt.plot(y, marker = '*',
         ms=20,
         mfc='blue',
         mec='blue')
plt.show()