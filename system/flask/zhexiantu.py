#-*-coding:utf-8-*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import matplotlib.pyplot as plt 
def zhexian():
    y1=[3.51,2.48,3.12,2.27,] 
    x1=[1,2,3,4]
    plt.xlim((0,8))
    plt.ylim((0,5)) 
    #x2=range(0,4) 
    #y2=[23,18,28,0] 
    plt.plot(x1,y1,label='GPA',linewidth=3,color='r',marker='o', 
    markerfacecolor='blue',markersize=12) 
    #plt.plot(x2,y2,label='second line') 
    plt.xlabel('XUEQI') 
    plt.ylabel('GPA') 
    plt.title(u'Students Score')
    for a, b in zip(x1, y1):  
        plt.text(a, b, (a,b), fontsize=10)   
    plt.legend()
    plt. savefig('/home/cris/system/flask/static/images/zhexiantu.png')
    #plt.show()

if __name__ == "__main__":
    zhexian() 

