#coding:utf-8
import numpy as np
import cv2
from PIL import Image
def getPoint(x,y,data,subdata=None):
    a=[0,-1,0,1,0,-2,0,2,0,-3,0,3,0,-4,0,4,0,-5,0,5]
    b=[1,0,-1,0,2,0,-2,0,3,0,-3,0,4,0,-4,0,5,0,-5,0]
    width,height=data.shape
    if subdata is None:
        subdata=[]
    if x>5 and y<height-5 and y>5 and x<width-5:
        for i in range(20):
            if data[x+a[i]][y+b[i]]==1:
                subdata.append((x+a[i],y+b[i]))
                data[x+a[i]][y+b[i]]=2
                getPoint(x+a[i],y+b[i],data,subdata)
    subdata.append((x,y))
 
def getcell(data):
    list1=[]
    index=0
    flag=True
    for y in range(data.shape[1]):
        for x in range(data.shape[0]):
            if data[x][y]==1:
                if list1:
                    for i in range(len(list1)):
                        if (x,y) in list1[i]:
                            flag=False
                if not flag:
                    continue
                list1.append([])
                getPoint(x,y,data,list1[index])
                index+=1
            else :
                continue
    
    for index in range(len(list1)):
        l=list1[index][0][0]
        t=list1[index][0][1]
        r=list1[index][0][0]
        b=list1[index][0][1]
        for i in list1[index]:
            x=i[0]
            y=i[1]
            l=min(l,x)
            t=min(t,y)
            r=max(r,x)
            b=max(b,y)
        w=r-l+1
        h=b-t+1
        if (w*h <8):#去除小色块
            continue
        img0=np.zeros([w,h])#创建全0矩阵
        for x,y in list1[index]:
            img0[x-l][y-t]=1
        img0[img0<1]=255
        img1=Image.fromarray(img0)
        img1=img1.convert('RGB')
        img1.save('/home/cris/Study/text/images/'+str(index)+'.png')

if __name__=="__main__":

    data = cv2.imread("/home/cris/Study/text/AI/MNIST/image/954n.png",2)
    allimg=getcell(data)










