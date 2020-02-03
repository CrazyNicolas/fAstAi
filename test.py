import streamlit as st
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
# data prepare
# df = pd.read_csv('E:\\pycode\\Semantic_Segmentation_cnn\\train\\data.csv')

map_data = pd.DataFrame(np.random.randn(1000,2)/[50,50]+ [29.58,113.41]
	,columns=['lat','lon'])

# work region
st.title('\tMy first app')

st.write('Here is our first attempt at using data to create a table:')
# df

st.header('This is a example of map:')
st.map(map_data)

st.subheader('检验一下中文显示，顺便看一下复选框的功能')
if st.checkbox('Show dataframe'):
	chart_data = pd.DataFrame(np.random.randn(20,3),
		columns = ['a','b','c'])
	st.line_chart(chart_data)

# st.write('使用列表选择框')

# option = st.selectbox(
#  	'Which number do you like best?',
#  	[1,2,3,4,5,6,7,8,9]
#  	)
# 'your option',option
st.write('使用列表选择框,但将其放在侧栏为了美观')

option = st.sidebar.selectbox(
 	'Which number do you like best?',
 	[1,2,3,4,5,6,7,8,9]
 	)
'your option',option

# # 另外一种可以写字的栏
# latest_iteration = st.empty()
# bar = st.progress(0)

# # 进度条
# for i in range(100):
# 	latest_iteration.text(f'Iterration {i+1}')
# 	bar.progress(i+1)
# 	time.sleep(0.1)
# latest_iteration.text('We are DONE!')

st.header('引入代码块')
code_block = '''def main():
...  print(a+b)'''
st.code(code_block,language='python')

st.header('使用matplotlib作图')
x = np.random.randn(100)
y = np.random.randn(100)
fig = plt.figure()
plt.scatter(x,y)
st.pyplot(fig)

# 按钮
btn = st.button('点击显示图片')
with st.echo():
	st.header('对按钮的使用')
 	
 	
 
img = np.random.randn(224,224)
img = np.clip(img,0,1)
if btn:
	st.image('http://img1.imgtn.bdimg.com/it/u=3861925707,2023347812&fm=26&gp=0.jpg',caption='从网上获取的图片')
else:
	st.image(img,'一张随机生成的图像')

# st.header('文件上传器')
# loader = st.file_uploader('Choose a csv file',type = ['csv'])
# with st.spinner('Wait for it...'):
# 	data = pd.read_csv(loader) if loader is not None else None
# 	st.dataframe(data)
# st.success('Done!')

st.balloons()

