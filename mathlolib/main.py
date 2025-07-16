import matplotlib.pyplot as plt 
import numpy as np

data=[90,76,56,47,55,89,78,76,46,87,98,67,56,98,78,66,87,67]


t=np.linspace(0,len(data),len(data))
data.sort()
y=np.array(data)
plt.plot(t,y)
plt.show()
