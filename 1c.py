import matplotlib.pyplot as plt
import math
import numpy as np

import math

x = [1,14,15,26,30,46]
y = [math.log10(94 *10**6),
     math.log10(1.5*10**9),
     math.log10(8.3*10**9),
     math.log10(17 *10**9),
     math.log10(175*10**9),
     math.log10(530*10**9)]

def average(list):
    total = 0
    for i in range(len(list)):
        total += list[i]
    return (total / len(list))

x_average = average(x)
y_average = average(y)

def calc_s (list1,list2,average1,average2):
    total = 0
    for i in range(len(list1)):
        total += (list1[i]-average1)*(list2[i]-average2)
    return total

sxx = calc_s(x,x,x_average,x_average)
syy = calc_s(y,y,y_average,y_average)
sxy = calc_s(x,y,x_average,y_average)

BHat = sxy/sxx
alpha = y_average - x_average*BHat

zx = np.linspace(0,50,10000)
f = BHat*zx+alpha

print(BHat)
print(alpha)

plt.scatter(x,y)
plt.plot(zx,f)

plt.ylabel('Parameters log 10')
plt.xlabel('Year')

plt.show()