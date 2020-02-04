import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from io import BytesIO
'fAstAi@mzy'
'this is ver 1.0'
'https://github.com/SCUTBlockChainResearchTeam/fAstAi'

option = st.sidebar.selectbox('章节',['第一章','也许有第二章','等你来谱写新的篇章'])
if option == '第一章':
	pass
else:
	st.balloons()
lower_blue = np.array([100, 110, 110])
upper_blue = np.array([130, 255, 255])
lower_green = np.array([50,110,110])
upper_green = np.array([70,255,255])
lower_red = np.array([0,110,110])
upper_red = np.array([10,255,255])
# 根据想要筛选的范围把区域提取出来
def extract_by_color(hsv_img, low, high):
	# 造一层掩膜出来 output的size不变 但是在范围里的变成255，不在的变成0
	mask = cv2.inRange(hsv_img, low, high)
	# 保留我们需要的区域
	result = cv2.bitwise_and(hsv_img,hsv_img,mask=mask)

	# 绘图做对比
	plt.cla()
	plt.subplot(1,3,1)
	plt.axis('off')
	plt.imshow(hsv_img)
	plt.title('HSV')
	plt.subplot(1,3,2)
	plt.axis('off')
	plt.imshow(mask)
	plt.title('MASK')
	plt.subplot(1,3,3)
	plt.axis('off')
	plt.imshow(result)
	plt.title('RESULT')
	st.pyplot()


def display(image, low_bound, high_bound):
	hsv_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
	extract_by_color(hsv_image,low_bound,high_bound)


st.markdown('<h1><center>图像的颜色空间转换</center><h1>'
	,unsafe_allow_html = True)

st.markdown('# 典型颜色空间的转换')

st.markdown('## 从BGR三通道到GRAY单通道\n> BGR是RGB的逆序，这是opencv的图像格式\
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
st.markdown('## 从BGR三通道到HSV三通道\n> 实际上，HSV三通道是更符合我们人类感官\
	的一种颜色表达形式。H代表色调，是用0-179表示从暖到冷的不同色调；S代表饱和度，V代表亮度。\
	具体的样子可以参见下图：')
st.image('http://img2.imgtn.bdimg.com/it/u=2865655404,3600196686&fm=26&gp=0.jpg')

st.markdown('> `cv2.cvtColor()`函数这个时候又要登场了，众所周知我们不管是用[PIL](https://www.liaoxuefeng.com/wiki/897692888725344/966759628285152)还是直接用\
	`cv2.imread()`函数都是讲图片读取为BGR/RGB格式，很自然的，现在我们要将其转化为\
	HSV格式。 下面展示一个案例来引出本章的***核心知识点***：\n>> 现在我们面临的场景是这样的:\
	给定一张图片，我们想要把其中的某个特定颜色范围的图像筛选出来，术语上，这种操作叫做\
	颜色识别追踪。这个时候我们需要做的事情可以分为三步：\n>>> 1. **确定颜色范围**：用一个例子来说明，假如你想筛选蓝色区域，那么首先构造一个蓝色的像素点，`[[[255,0,0]]]`，注意\
	注意是BGR，其次是三通道，所以才有三个中括号。(讲这么直白是为了大家理解)接下来使用如下语句\
	`cv2.cvtColor(pixel,cv2.COLOR_BGR2HSV)`就可以知道蓝色对应的HSV值。再根据上面的圆锥形模型就可以知道我们可以\
	设置一个上下界,这就是我们的范围。\n2. **在图像上找到这些颜色范围**：实际上找颜色范围用到的函数是`cv2.inrange()`。\
	这是比较容易理解的地方，唯一需要注意的就是input和你的筛选标准的维度的匹配，细心的同学可以思考一下下面代码部分各参数的维数。\n3. **利用第二步中找到的区域把原图其他地方~~灭掉~~**：其实这一步会让人头晕，为什么要用这个\
	`bitwise_and()`函数(按位与)呢？这就涉及到要去官方文档看一下具体的调用了，在这里先大概说一下\
	，这里是利用bitwise系列函数里面有一个可选参数mask，函数会根据这个mask来决定把原图中mask的部分按位与操作，其他地方直接舍弃掉\
	这样就达到了我们想要的目的。当然这里也可以使用`bitwise_or`函数（按位或）。聪明的同学应该已经想到为什么了吧。')
code = '''blue = np.uint8([[[255, 0, 0]]])
hsv_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
print(hsv_blue)  # [[[120 255 255]]] 这就是将蓝色的像素点转化过来变成这种形式
# 1.蓝色的范围，不同光照条件下不一样，可灵活调整
lower_blue = np.array([100, 110, 110])
upper_blue = np.array([130, 255, 255])
# 2.从BGR转换到HSV
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# 3.inRange()：介于lower/upper之间的为白色，其余黑色
mask = cv2.inRange(hsv, lower_blue, upper_blue)
# 4.只保留原图中的蓝色部分
res = cv2.bitwise_and(frame, frame, mask=mask)'''
st.code(code,language='python')
st.markdown('## 图像颜色识别小案例')
lena_or_not = st.radio('使用默认照片或上传？',
	('默认','上传'))
if lena_or_not == '默认':
	img_mmm = cv2.imread('lena.jpg')
	choosen_color = st.radio('选择想要识别的颜色',
		('blue','green','red'))
	if choosen_color == 'blue':
		display(img_mmm, lower_blue,upper_blue)
	if choosen_color == 'red':
		display(img_mmm, lower_red,upper_red)
	if choosen_color == 'green':
		display(img_mmm, lower_green,upper_green)
else:
	file = st.file_uploader('请选择一张你的照片',type=["jpg","png"])
	if file is not None:
		data = file.read()
		rgb_img = cv2.imdecode(np.frombuffer(data, np.uint8), cv2.IMREAD_COLOR)
		img_up = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2BGR)
		# img_up = cv2.cvtColor(img_up,cv2.COLOR_RGB2BGR)
		choosen = st.radio('选择想要识别的颜色',
		('blue','green','red'))
		if choosen == 'blue':
			display(img_up, lower_blue,upper_blue)
		if choosen == 'red':
			display(img_up, lower_red,upper_red)
		if choosen == 'green':
			display(img_up, lower_green,upper_green)





st.markdown('<h1><center>本章关键函数</center><h1>'
	,unsafe_allow_html = True)
st.markdown('这里只会告诉你官方文档具体函数的位置链接，钻研靠自己！\n> 1. [cv2.cvtColor()](https://docs.opencv.org/4.0.0/d8/d01/group__imgproc__color__conversions.html#ga397ae87e1288a81d2363b61574eb8cab)\
	2. [cv2.inRange()](https://docs.opencv.org/4.0.0/d2/de8/group__core__array.html#ga48af0ab51e36436c5d04340e036ce981)\
	3. [cv2.bitwise_and()](https://docs.opencv.org/4.0.0/d2/de8/group__core__array.html#ga60b4d04b251ba5eb1392c34425497e14)')


