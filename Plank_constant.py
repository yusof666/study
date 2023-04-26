import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
from scipy.optimize import curve_fit##自定义函数进行拟合
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False##解决负号显示问题
def func_poly_1(x,a,b):
    return a*x+b
u_s=np.array([-1.889,-1.604,-1.311,-0.767,-0.647])
v=np.array([8.214,7.408,6.879,5.490,5.196])
popt,pcov=curve_fit(func_poly_1,v,u_s)
plt.figure()
plt.plot(v,[func_poly_1(i,*popt) for i in v])
plt.title('U_s-v图')
plt.xlabel('v(10^4Hz)')
plt.ylabel('U_s(v)')
plt.show()

I=np.array([0,1,2,3,4,4,5,5,6,7,8,11,16,19,22,24,32,38,43,48,52,55])
U=np.array([-1.3,-1,-0.7,-0.4,-0.1,0,0.2,0.4,0.6,0.8,1,2,3,4,5,6,10,14,18,22,26,30])
x_new_2=np.linspace(U.min(),U.max(),300)
func_2=interp1d(U,I,kind='cubic')
y_new_2=func_2(x_new_2)
plt.figure()
plt.plot(x_new_2,y_new_2)
plt.xlabel('U(v)')
plt.ylabel('I(A)')
plt.title('I-U伏安特性曲线图')
plt.show()



