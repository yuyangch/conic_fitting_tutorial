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

print data_points
#print data_piints[0][0]


A_9=[[4.0,0.0,2.0,0.0,0.0,0.0,2.0,0.0,1.0],
   [0.0,0.0,0.0,0.0,4.0,2.0,0.0,2.0,1.0],
   [4.0,0.0,-2.0,0.0,0.0,0.0,-2.0,0.0,1.0],
   [0.0,0.0,0.0,0.0,4.0,-2.0,0.0,-2.0,1.0],
   [2.0,2.0,1.414,2.0,2.0,1.414,1.414,1.414,1.0]
   ]


#A_si=[4.0]

#A_6=[[4.0,0.0,1.0,0.0,4.0,0.0],
#       [0.0,4.0,1.0,0.0,0.0,4.0],
#       [4.0,0.0,1.0,0.0,-4.0,0.0],
#       [0.0,-4.0,1.0,0.0,0.0,-4.0],
#       [2.0,2.0,1.0,4.0,2.828,2.828],
#   ]




J=np.matrix(A_9)   #J=d(Ax)/dx=A

U,S,Vh=linalg.svd(J)

print "U=",U,"S=",S,"Vh=",Vh

#starting with a unit circle
#C_initial_6=np.matrix([[1.0],
#		     [1.0],
#		     [-1.0],
#		     [0.0],
#		     [0.0],
#		     [0.0]	
#			])


C_initial_9=np.matrix([[2.0],
		     [5.0],
		     [0.0],
		     [5.0],
		     [1.0],
		     [0.0],
		     [0.0],
		     [0.0],
		     [-1.0]		
			])
#C_initial_9=np.matrix()
print C_initial_9

for i in range(0,2000):
	e=J*C_initial_9
	print "e",e
	delta_c=(-1.0)*J.transpose()*linalg.inv(J*J.transpose())*e    #(4.11-p99) in M.G

	#delta_c1=(-1.0)*linalg.inv(J.transpose()*J)*J.transpose()*e
	print "delta_c",delta_c
	C_initial_9=C_initial_9+delta_c
	print "C_initial_9",C_initial_9




#rospy.init_node('listener', anonymous=True)
point =np.matrix([[1.414],[1.414],[1.0]])

#data_points.append(np.matrix([[1.414],[1.414],[1.0]]))
error=point[0,0]*point[0,0]*C_initial_9[0,0]+point[0,0]*point[1,0]*C_initial_9[1,0]+point[0,0]*point[2,0]*C_initial_9[2,0]+point[0,0]*point[1,0]*C_initial_9[3,0]+point[1,0]*point[1,0]*C_initial_9[4,0]+point[1,0]*point[2,0]*C_initial_9[5,0]+point[0,0]*point[2,0]*C_initial_9[6,0]+point[1,0]*point[2,0]*C_initial_9[7,0]+point[2,0]*point[2,0]*C_initial_9[8,0]

print "error ",error

