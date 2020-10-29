#!/usr/bin/env python2

import numpy as np
import matplotlib.pyplot as pl
from scipy import linalg
from copy import deepcopy

data_points=[]

data_points.append(np.matrix([[2.0],[0.0],[1.0]]))
data_points.append(np.matrix([[0.0],[2.0],[1.0]]))
data_points.append(np.matrix([[-2.0],[0.0],[1.0]]))
data_points.append(np.matrix([[0.0],[-2.0],[1.0]]))

data_points.append(np.matrix([[1.414],[1.414],[1.0]]))
#data_points.append(np.matrix([[1.41421356237],[1.41421356237],[1.0]]))

#data_points.append(np.matrix([[-1.41421356237],[-1.41421356237],[1.0]]))




#print data_points

C_collections=[]

C_initial_9=np.matrix([[1.0],
		     [0.0],
		     [0.0],
		     [0.0],
		     [1.0],
		     [0.0],
		     [0.0],
		     [0.0],
		     [-1.0]		
			])
for iterations in range(0,25):
	C_collections.append(deepcopy(C_initial_9))
	J=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
	e=0
	for point in data_points:
		#print point[0,0]
		#print point[1]
		#print "point",point
		#e_point=
		num=(point[0,0]*point[0,0]*C_initial_9[0,0]+point[0,0]*point[1,0]*C_initial_9[1,0]+point[0,0]*point[2,0]*C_initial_9[2,0]+
			     point[0,0]*point[1,0]*C_initial_9[3,0]+point[1,0]*point[1,0]*C_initial_9[4,0]+point[1,0]*point[2,0]*C_initial_9[5,0]+
			     point[0,0]*point[2,0]*C_initial_9[6,0]+point[1,0]*point[2,0]*C_initial_9[7,0]+point[2,0]*point[2,0]*C_initial_9[8,0])**2
		#print "num",num
		num_dot_factor=2.0*(point[0,0]*point[0,0]*C_initial_9[0,0]+point[0,0]*point[1,0]*C_initial_9[1,0]+point[0,0]*point[2,0]*C_initial_9[2,0]+
			     point[0,0]*point[1,0]*C_initial_9[3,0]+point[1,0]*point[1,0]*C_initial_9[4,0]+point[1,0]*point[2,0]*C_initial_9[5,0]+
			     point[0,0]*point[2,0]*C_initial_9[6,0]+point[1,0]*point[2,0]*C_initial_9[7,0]+point[2,0]*point[2,0]*C_initial_9[8,0])
		#print "num_dot_factor",num_dot_factor
		denom=4*((point[0,0]*C_initial_9[0,0]+point[1,0]*C_initial_9[1,0]+point[2,0]*C_initial_9[2,0])**2+
			 (point[0,0]*C_initial_9[3,0]+point[1,0]*C_initial_9[4,0]+point[2,0]*C_initial_9[5,0])**2 )
		#print "denom",denom
		denom_dot_factor=[]
		denom_dot_1=8*(point[0,0]*C_initial_9[0,0]+point[1,0]*C_initial_9[1,0]+point[2,0]*C_initial_9[2,0])
		denom_dot_2=8*(point[0,0]*C_initial_9[3,0]+point[1,0]*C_initial_9[4,0]+point[2,0]*C_initial_9[5,0])
		denom_dot_factor.append(denom_dot_1)
		denom_dot_factor.append(denom_dot_2)
		#print "denom_dot_factor",denom_dot_factor
		
		e_point=num/denom
		#print "e_point",e_point
		e=e+e_point
		for i in range (0,3):
			for j in range(0,3):
				J_index=i*3+j
				num_index_1=i
				num_index_2=j
				denom_index_1=i
				denom_index_2=j
				num_dot=num_dot_factor*point[num_index_1,0]*point[num_index_2,0]
				#print "i",i,"j",j,"num_dot",num_dot
				if i<2:
					denom_dot=denom_dot_factor[denom_index_1]*point[denom_index_2,0]
				else:		
					denom_dot=0.0
				#print "denom_dot",denom_dot
				d_num_denom=(denom*num_dot-num*denom_dot)/(denom**2)
				J[J_index]=J[J_index]+d_num_denom
				#print J


	J=np.matrix([J])

	#delta_c=

	delta_c=(-0.25)*J.transpose()*linalg.inv(J*J.transpose())*e    #(4.11-p99) in M.G

	#delta_c1=(-1.0)*linalg.inv(J*J.transpose())*J.transpose()*e

	#print delta_c
	C_initial_9=C_initial_9+delta_c
	print C_initial_9





#print data_piints[0][0]

point =np.matrix([[1.414],[1.414],[1.0]])

#data_points.append(np.matrix([[1.414],[1.414],[1.0]]))
error=point[0,0]*point[0,0]*C_initial_9[0,0]+point[0,0]*point[1,0]*C_initial_9[1,0]+point[0,0]*point[2,0]*C_initial_9[2,0]+point[0,0]*point[1,0]*C_initial_9[3,0]+point[1,0]*point[1,0]*C_initial_9[4,0]+point[1,0]*point[2,0]*C_initial_9[5,0]+point[0,0]*point[2,0]*C_initial_9[6,0]+point[1,0]*point[2,0]*C_initial_9[7,0]+point[2,0]*point[2,0]*C_initial_9[8,0]

print "error ",error

#####################################################################PLOTTING#############################################3333

fig=pl.figure(figsize=(17,17))
for p in data_points:
	pl.plot(p[0,0],p[1,0],marker='+',markersize=30,color="black")
#fig=pl.figure(figsize=(5,5))
x = np.linspace(-2.5, 2.5, 50)
y = np.linspace(-2.5, 2.5, 50)

X, Y = np.meshgrid(x, y)

color_delta=1.0/len(C_collections)
i=0
for C in C_collections:
	i=i+1
	a=C[0,0]
	b=C[1,0]+C[3,0]
	c=C[4,0]
	d=C[2,0]+C[6,0]
	e=C[5,0]+C[7,0]
	f=C[8,0]
	Z = a*X**2+b*X*Y+c*Y**2+d*X+e*Y+f
	pl.contour(X, Y, Z, [0], colors=[(i*color_delta,1-i*color_delta,1-i*color_delta)])

pl.title("Starting Conics colored approaches Blue, Ending Conics approaches Red")
pl.show()
