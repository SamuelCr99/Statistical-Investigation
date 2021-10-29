import matplotlib.pyplot as plt
import numpy as np

x = [2018+1/12,2019+2/12,2019+3/12,2020+2/12,2020+6/12,2021+10/12]
y = [94*10**6,1.5*10**9,8.3*10**9,17*10**9,175*10**9,530*10**9]

BHat = 0.08427335479400888
alpha = 8.190329535314607 
zx = np.linspace(2017,2022,1000000)
f = BHat*zx+alpha

plt.scatter(x,y)
plt.plot(zx,f)
plt.ylabel('Parameters')
plt.xlabel('Year')
plt.show()
