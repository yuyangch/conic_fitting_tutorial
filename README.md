# conic_fitting_tutorial
In Chapter 4 of the book Multiple View Geometry by Richard Hartley there is an conic fitting example (Example 4.2-p99)
Where the Sampson Error is derived. However the book did not go into detail of how to iterate over the parameters of the conic. In order to arrive at the fitted conic, This tutorial explore two approaches. Also it briefly covers how to iterate over data points to find  <img src="https://render.githubusercontent.com/render/math?math=\hat{X}"> the closest point on conic <img src="https://render.githubusercontent.com/render/math?math=C"> to the measure point <img src="https://render.githubusercontent.com/render/math?math=X">

Before starting note the notation: 

<img src="https://render.githubusercontent.com/render/math?math=x=[x',y',w']^{T}">  is in 2D homogenous coordinate and 

<img src="https://render.githubusercontent.com/render/math?math=C">   is a 3x3 matrix representing the conic (see 2.2.3-p30)

# Approach 1 Iteration Using the Original Error Function <img src="https://render.githubusercontent.com/render/math?math=x^{T}Cx">
The goal here is to iterate over parameters of  <img src="https://render.githubusercontent.com/render/math?math=C"> instead of <img src="https://render.githubusercontent.com/render/math?math=x">. The calculation of <img src="https://render.githubusercontent.com/render/math?math=\delta_{x}">  is the same as (4.11)-p99, therefore a Jacobian over parameters of <img src="https://render.githubusercontent.com/render/math?math=C"> is needed

First convert <img src="https://render.githubusercontent.com/render/math?math=x^{T}Cx"> to the form of <img src="https://render.githubusercontent.com/render/math?math=Ac=0"> where <img src="https://render.githubusercontent.com/render/math?math=A"> is an nx9 matrix (n being the number of data points) and <img src="https://render.githubusercontent.com/render/math?math=Ac=0"> where <img src="https://render.githubusercontent.com/render/math?math=c"> is the vectorization of conic <img src="https://render.githubusercontent.com/render/math?math=C"> where <img src="https://render.githubusercontent.com/render/math?math=c=[C_{11},  C_{12} , C_{13} , C_{21} , C_{22} ,C_{23}, C_{31}, C_{32}, C_{33}]^{T}"> (in the same manner as  h vector in (4.1)-p89)  Therefore for a single point <img src="https://render.githubusercontent.com/render/math?math=x">, the rewrite is: <img src="https://render.githubusercontent.com/render/math?math=Ac=[x'*x^{T},y'*x^{T},w'*x^{T}]c"> where <img src="https://render.githubusercontent.com/render/math?math=x'*x^{T}"> is a 1x3 vector

the Jacobian of <img src="https://render.githubusercontent.com/render/math?math=Ac"> over <img src="https://render.githubusercontent.com/render/math?math=c"> is simply <img src="https://render.githubusercontent.com/render/math?math=A">. Therefore to calculate a correction of <img src="https://render.githubusercontent.com/render/math?math=c">, using  (4.11)-p99, <img src="https://render.githubusercontent.com/render/math?math=\delta_{c}=-A^{T}(AA^{T})^{-1}\epsilon">   

Note:<img src="https://render.githubusercontent.com/render/math?math=\epsilon">is a nx1 vector, each element correspond the a point <img src="https://render.githubusercontent.com/render/math?math=x"> residual, so <img src="https://render.githubusercontent.com/render/math?math=\epsilon=x^{T}Cx">




