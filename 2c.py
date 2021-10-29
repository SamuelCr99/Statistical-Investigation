import matplotlib.pyplot as plt
import math


x = [1,14,15,26,30,46]
y = [math.log10(94 *10**6),
     math.log10(1.5*10**9),
     math.log10(8.3*10**9),
     math.log10(17 *10**9),
     math.log10(175*10**9),
     math.log10(530*10**9)]
plt.scatter(x,y)

#plt.axis([0, 6, 0, 20])
plt.ylabel('Parameters log 10')
plt.xlabel('Year')

plt.show()