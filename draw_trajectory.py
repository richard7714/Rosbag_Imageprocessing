import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

f = open("2022-09-29-2nd_floor_1_2X.txt","r")
lines = f.readlines()
x,y,z=[],[],[]
for i in lines:
    pose = i.split(" ")[1:4]
    x.append(float(pose[0]))
    z.append(float(pose[1]))
    y.append(float(pose[2]))
    
# fig = plt.figure()
# plt.plot(x,y)
# plt.show()

fig2 = plt.figure()
ax = fig2.add_subplot(111,projection='3d')
ax.plot(x,y,z)
plt.show()