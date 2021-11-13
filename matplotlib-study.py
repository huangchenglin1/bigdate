import ax as ax
import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits.axisartist as axisartist
#创建画布
fig = plt.figure(figsize=(8, 8))
#使用axisartist.Subplot方法创建一个绘图区对象ax
ax = axisartist.Subplot(fig, 111)
#将绘图区对象添加到画布中
fig.add_axes(ax)
x=np.linspace(-2*np.pi,2*np.pi,100)
y=np.linspace(-2,2,100)
# 构建两个列表
# a = [1,3,5,7,9]
# b = [2,4,6,8,10]
# c = [2,9,5,3,7]
# d = [3,9,2,1,1]
# 创建一个画布
# figure = plt.figure()
# ax = plt.subplot(2,2,1)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlim(-2*np.pi,2*np.pi)
ax.set_ylim(-2,2)
ax.axis[:].set_visible(False)
ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))
ax.plot(x,np.sin(x),label="y=sinx")
#ax.new_floating_axis代表添加新的坐标轴
ax.axis['x'] = ax.new_floating_axis(0,0)
#给x坐标轴加上箭头
ax.axis['x'].set_axisline_style('->',size = 1)
#添加y坐标轴，且加上箭头
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("-|>", size = 1.0)
plt.legend()
#设置x、y轴上刻度显示方向
ax.axis["x"].set_axis_direction("bottom")
ax.axis["y"].set_axis_direction("right")
plt.show()
