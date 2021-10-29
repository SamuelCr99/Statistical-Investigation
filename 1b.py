import matplotlib.pyplot as plt


x = [2018+1/12,2019+2/12,2019+3/12,2020+2/12,2020+6/12,2021+10/12]
y = [94*10**6,1.5*10**9,8.3*10**9,17*10**9,175*10**9,530*10**9]
plt.scatter(x,y)

#plt.axis([0, 6, 0, 20])
plt.ylabel('Parameters')
plt.xlabel('Year')
plt.show()