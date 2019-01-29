#-*-coding:utf-8-*-
import matplotlib.pyplot as plt  
import random
x1 = list(range(5))
y1 = [5,6,9,1,3]  
plt.plot(x1, y1,  color='r',markerfacecolor='blue')  
for a, b in zip(x1, y1):  
    plt(a, b, (a,b), fontsize=10)  
 
plt.legend()  
plt.show()
