#-*-coding:utf-8-*-
from PIL import Image, ImageFilter
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import cv2
import Image


def sum_9_region_new(img, x, y):
	'''确定噪点 '''
	cur_pixel = img.getpixel((x, y))  # 当前像素点的值
	width = img.width
	height = img.height
 
	if cur_pixel == 1:  # 如果当前点为白色区域,则不统计邻域值
		return 0
 
	# 因当前图片的四周都有黑点，所以周围的黑点可以去除
	if y < 3:  # 本例中，前两行的黑点都可以去除
		return 1
	elif y > height - 3:  # 最下面两行
		return 1
	else:  # y不在边界
		if x < 3:  # 前两列
			return 1
		elif x == width - 1:  # 右边非顶点
			return 1
		else:  # 具备9领域条件的
			sum = img.getpixel((x - 1, y - 1)) \
				  + img.getpixel((x - 1, y)) \
				  + img.getpixel((x - 1, y + 1)) \
				  + img.getpixel((x, y - 1)) \
				  + cur_pixel \
				  + img.getpixel((x, y + 1)) \
				  + img.getpixel((x + 1, y - 1)) \
				  + img.getpixel((x + 1, y)) \
				  + img.getpixel((x + 1, y + 1))
			return 9 - sum
 
def collect_noise_point(img):
	'''收集所有的噪点'''
	noise_point_list = []
	for x in range(img.width):
		for y in range(img.height):
			res_9 = sum_9_region_new(img, x, y)
			if (0 < res_9 < 3) and img.getpixel((x, y)) == 0:  # 找到孤立点
				pos = (x, y)
				noise_point_list.append(pos)
	return noise_point_list
 
def remove_noise_pixel(img, noise_point_list):
	'''根据噪点的位置信息，消除二值图片的黑点噪声'''
	for item in noise_point_list:
		img.putpixel((item[0], item[1]), 1)
 
def get_bin_table(threshold=115):
	'''获取灰度转二值的映射table,0表示黑色,1表示白色'''
	table = []
	for i in range(256):
		if i < threshold:
			table.append(0)
		else:
			table.append(1)
	return table
 
def main1():
    
	image = Image.open('/home/cris/AI/MNIST/image/zd4.jpg')  
	imgry = image.convert('L')
	table = get_bin_table()
	binary = imgry.point(table, '1')
	noise_point_list = collect_noise_point(binary)
	remove_noise_pixel(binary, noise_point_list)
	binary.save('/home/cris/AI/MNIST/image/finaly.png')
	binary.show()


# 裁剪字符
def cut(img):
    # 查找检测物体的轮廓
    image, contours, hierarchy = cv2.findContours(img, 2, 2)
    cv2.imshow('image',image)
    # 计数器
    flag = 1
    for cnt in contours:
        # 最小的外接矩形, cnt是一个二值图, x,y是矩阵左上点的坐标, w,h是矩阵的宽和高
        x, y, w, h = cv2.boundingRect(cnt)
        # 画出矩形(图片，矩形左上角，矩形右下角，线框的颜色，线宽)
        #cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        '''# 用红色表示有旋转角度的矩形框架
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
        cv2.imwrite('contours.png', img)
        '''
        # x，y的值不能为0以及图片的大小要超过28*28(按照需求自己设置)，不然我们会得到其他的不想要的图片
        if x != 0 and y != 0 and w*h >= 800:
            print((x,y,w,h))
            # 调整图像尺寸为28*28
            resize_img = cv2.resize(img[y:y+h, x:x+w], (28,28))
            # 再次二值化
            im_fixed = thresh_old(resize_img, 200, 255)
            # 保存图片
            cv2.imwrite('out_img/char.png',resize_img)
            cv2.imwrite('out_img/resize.png',im_fixed)
            flag += 1

 # 二值化处理
def thresh_old(img, l=100, h=255):
    ret,im_fixed=cv2.threshold(img,l,h,cv2.THRESH_BINARY)
    #im_fixed = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 1)
    return im_fixed

#灰度化处理
def cvt_Color(img):
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return img

if __name__=='__main__':
    main1()
    img = cv2.imread('image/finaly.png')
    gary = cvt_Color(img)
    thresh = thresh_old(gary)
    cut(thresh)
   





