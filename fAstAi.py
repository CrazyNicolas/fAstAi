import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
"""
fAstAi@mzy
this is ver 1.0
"""

st.markdown('<h1><center>图像的颜色空间转换</center><h1>'
	,unsafe_allow_html = True)

st.markdown('# 典型颜色空间的转换')

st.markdown('## 从BGR三通道到GRAY图\n> BGR是RGB的逆序，这是opencv的图像格式\
	，虽然有些奇葩但也不是特别难记。而且opencv的数据格式本身就是**numpy数组**，\
	如果有~~强迫症~~的同学，也不是不可以考虑使用numpy的index方法`img[:,:,::-1]`\
	来转换为RGB。其实转化成灰度图是一件很简单的事只不过我们这里突出`cvtColor()`\
	这个函数,因为这个函数不光可以转化灰度图，还能转化后面我们要讲的HSV空间模型，还有\
	数不尽的格式可以转化，有**性**趣的同学可以去查看[官方文档](https://docs.opencv.org/)')
with st.echo():
	import cv2
	img = cv2.imread('lena.jpg') # 可以追加参数直接读灰度 imread('lena.jpg',0) 默认为1
	# 转换为灰度图
	img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	plt.subplot(1,2,1)
	plt.axis('off')
	plt.imshow(img)
	plt.title('BGR')
	plt.subplot(1,2,2)
	plt.axis('off')
	plt.imshow(img_gray)
	plt.title('GRAY')
	st.pyplot()
st.subheader('追踪视频或者图片里特定颜色的区域/物体')
st.subheader('了解两个OpenCV的重要函数')


