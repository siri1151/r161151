#-----generating plots using numpy-------
import numpy as np
a=np.array([1,5,2,5-2.3,0])
from matplotlib import pyplot as plt
b=np.sin(a)
plt.subplot(2,1,1)
plt.plot(b,a)
plt.xlabel('time')
plt.ylabel('amplitude')
plt.title('continous time signal')
plt.subplot(2,1,2)
plt.stem(b,a)
plt.xlabel('discrete time')
plt.ylabel('amplitude')
plt.title('discrete signal')
plt.show()



