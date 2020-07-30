# conic_fitting_tutorial
In Chapter 4 of the book Multiple View Geometry by Richard Hartley there is an conic fitting example (Example 4.2-p99)
Where the Sampson Error is derived. However the book did not go into detail of how to iterate over the parameters of the conic. In order to arrive at the fitted conic, This tutorial explore two approaches. Also it briefly covers how to iterate over data points to find  <img src="https://render.githubusercontent.com/render/math?math=\hat{x}"> the closest point on conic <img src="https://render.githubusercontent.com/render/math?math=C"> to the measure point <img src="https://render.githubusercontent.com/render/math?math=x">

Before starting note the notation: 

<img src="https://render.githubusercontent.com/render/math?math=x=[x',y',w']^{T}">  is in 2D homogenous coordinate and 

<img src="https://render.githubusercontent.com/render/math?math=C">   is a 3x3 matrix representing the conic (see 2.2.3-p30)

# Calculate <img src="https://render.githubusercontent.com/render/math?math=\hat{x}">, the closest point on conic to point <img src="https://render.githubusercontent.com/render/math?math=x">

The Jacobian <img src="https://render.githubusercontent.com/render/math?math=J"> (a 1x2 matrix) over <img src="https://render.githubusercontent.com/render/math?math=x"> is given in example4.2-p99, note that the second term is simply <img src="https://render.githubusercontent.com/render/math?math=2x^{T}C(0,1,0)^{T}">

you can test by starting with a unit circle, or <img src="https://render.githubusercontent.com/render/math?math=C=diag(1,1,-1)">, and pick a point, let's say <img src="https://render.githubusercontent.com/render/math?math=x=(2,0,1)^{T}"> , then calculate <img src="https://render.githubusercontent.com/render/math?math=\epsilon=x^{T}Cx=3">, then calculate <img src="https://render.githubusercontent.com/render/math?math=\delta_{x}=-J^{T}(JJ^{T})^{-1}\epsilon=-[4,0]^{T}([4,0][4,0]^{T})^{-1}3=[-.75,0]^{T}">

At the end of each iteration simply calculate a new <img src="https://render.githubusercontent.com/render/math?math=x= \delta_{x} \plus x">
first iteration gives a new point <img src="https://render.githubusercontent.com/render/math?math=x=(1.25,0,1)^{T}">

repeat the iteration and the result should coverge to <img src="https://render.githubusercontent.com/render/math?math=x=(1,0,1)^{T}">, the closest point on the unit circle to <img src="https://render.githubusercontent.com/render/math?math=x=(2,0,1)^{T}">

feel free to try other conic/points







# Approach 1 Iteration Using the Original Error Function <img src="https://render.githubusercontent.com/render/math?math=x^{T}Cx">
The goal here is to iterate over parameters of  <img src="https://render.githubusercontent.com/render/math?math=C"> instead of <img src="https://render.githubusercontent.com/render/math?math=x">. The calculation of <img src="https://render.githubusercontent.com/render/math?math=\delta_{x}">  is the same as (4.11)-p99, therefore a Jacobian over parameters of <img src="https://render.githubusercontent.com/render/math?math=C"> is needed

First convert <img src="https://render.githubusercontent.com/render/math?math=x^{T}Cx"> to the form of <img src="https://render.githubusercontent.com/render/math?math=Ac=0"> where <img src="https://render.githubusercontent.com/render/math?math=A"> is an nx9 matrix (n being the number of data points) and <img src="https://render.githubusercontent.com/render/math?math=Ac=0"> where <img src="https://render.githubusercontent.com/render/math?math=c"> is the vectorization of conic <img src="https://render.githubusercontent.com/render/math?math=C"> where <img src="https://render.githubusercontent.com/render/math?math=c=[C_{11},  C_{12} , C_{13} , C_{21} , C_{22} ,C_{23}, C_{31}, C_{32}, C_{33}]^{T}"> (in the same manner as  h vector in (4.1)-p89)  Therefore for a single point <img src="https://render.githubusercontent.com/render/math?math=x">, the rewrite is: <img src="https://render.githubusercontent.com/render/math?math=Ac=[x'*x^{T},y'*x^{T},w'*x^{T}]c"> where <img src="https://render.githubusercontent.com/render/math?math=x'*x^{T}"> is a 1x3 vector

the Jacobian of <img src="https://render.githubusercontent.com/render/math?math=Ac"> over <img src="https://render.githubusercontent.com/render/math?math=c"> is simply <img src="https://render.githubusercontent.com/render/math?math=A">. Therefore to calculate a correction of <img src="https://render.githubusercontent.com/render/math?math=c">, using  (4.11)-p99, <img src="https://render.githubusercontent.com/render/math?math=\delta_{c}=-A^{T}(AA^{T})^{-1}\epsilon">   

At the end of each iteration simply calculate a new <img src="https://render.githubusercontent.com/render/math?math=c= \delta_{c} \plus c">

Note:<img src="https://render.githubusercontent.com/render/math?math=\epsilon">is a nx1 vector, each element correspond the a point <img src="https://render.githubusercontent.com/render/math?math=x"> residual, so <img src="https://render.githubusercontent.com/render/math?math=\epsilon=x^{T}Cx">

the script fit_conic.py starts from a unit circle and points belong to a circle with radius 2, you can take a look at the resulting c vector. (note that one of the point(1.414,1.414,1)) is slightly off the circle because 1.414 is slightly off of square root of 2 which is 
~1.41421356237.. the <img src="https://render.githubusercontent.com/render/math?math=\epsilon=x^{T}Cx"> with this point is printed as variable "error" at the end, for a comparison later with 2nd approach.



# Approach 2 Iteration Using the Sampson Error Function <img src="https://render.githubusercontent.com/render/math?math=\epsilon^{T}(JJ^{T})^{-1}\epsilon">  (4.12-p99)

