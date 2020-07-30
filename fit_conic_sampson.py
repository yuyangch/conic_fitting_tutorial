#!/usr/bin/env python2

import numpy as np
import matplotlib.pyplot as pl
from scipy import linalg


data_points=[]

data_points.append(np.matrix([[2.0],[0.0],[1.0]]))
data_points.append(np.matrix([[0.0],[2.0],[1.0]]))
data_points.append(np.matrix([[-2.0],[0.0],[1.0]]))
data_points.append(np.matrix([[0.0],[-2.0],[1.0]]))

data_points.append(np.matrix([[1.414],[1.414],[1.0]]))
#data_points.append(np.matrix([[1.41421356237],[1.41421356237],[1.0]]))

#data_points.append(np.matrix([[-1.41421356237],[-1.41421356237],[1.0]]))




#print data_points



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
for iterations in range(0,2000):
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

	delta_c=(-1.0)*J.transpose()*linalg.inv(J*J.transpose())*e    #(4.11-p99) in M.G
	#delta_c1=(-1.0)*linalg.inv(J*J.transpose())*J.transpose()*e

	#print delta_c
	C_initial_9=C_initial_9+delta_c
	print C_initial_9





#print data_piints[0][0]

point =np.matrix([[1.414],[1.414],[1.0]])

#data_points.append(np.matrix([[1.414],[1.414],[1.0]]))
error=point[0,0]*point[0,0]*C_initial_9[0,0]+point[0,0]*point[1,0]*C_initial_9[1,0]+point[0,0]*point[2,0]*C_initial_9[2,0]+point[0,0]*point[1,0]*C_initial_9[3,0]+point[1,0]*point[1,0]*C_initial_9[4,0]+point[1,0]*point[2,0]*C_initial_9[5,0]+point[0,0]*point[2,0]*C_initial_9[6,0]+point[1,0]*point[2,0]*C_initial_9[7,0]+point[2,0]*point[2,0]*C_initial_9[8,0]

print "error ",error


#A_9=[[4.0,0.0,2.0,0.0,0.0,0.0,2.0,0.0,1.0],
#   [0.0,0.0,0.0,0.0,4.0,2.0,0.0,2.0,1.0],
#   [4.0,0.0,-2.0,0.0,0.0,0.0,-2.0,0.0,1.0],
#   [0.0,0.0,0.0,0.0,4.0,-2.0,0.0,-2.0,1.0],
#   [2.0,2.0,1.414,2.0,2.0,1.414,1.414,1.414,1.0]
#   ]


#J=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
