# FAST BOIDS
"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import random

# Deliberately terrible code for teaching purposes

boids_x=np.array([random.uniform(-450,50.0) for x in range(50)])
boids_y=np.array([random.uniform(300.0,600.0) for x in range(50)])
boid_x_velocities=np.array([random.uniform(0,10.0) for x in range(50)])
boid_y_velocities=np.array([random.uniform(-20.0,20.0) for x in range(50)])

def update_boids(xs, ys, xvs, yvs):
         

        xdiff = np.add.outer(xs,-xs)
        ydiff = np.add.outer(ys,-ys)
        
        xvdiff = np.add.outer(xvs,-xvs)
        yvdiff = np.add.outer(yvs,-yvs)
        
        distance=xdiff**2+ydiff**2
        
    	for i in range(len(xs)):
		for j in range(len(xs)):
			xvs[i] += xdiff[j,i]*0.01/len(xs)
			yvs[i] += ydiff[j,i]*0.01/len(xs)
	                if distance[i,j] < 100:
				xvs[i] += -xdiff[i,j]
				yvs[i] += -ydiff[i,j]
	                    

	for i in range(len(xs)):
		for j in range(len(xs)):
			if distance[i,j] < 10000:
				xvs[i]+=xvdiff[j,i]*0.125/len(xs)
				yvs[i]+=yvdiff[j,i]*0.125/len(xs)
				
				
	for i in range(len(xs)):
		xs[i] += xvs[i]
		ys[i] += yvs[i]                      


figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(boids_x,boids_y)

def animate(frame):
   update_boids(boids_x,boids_y,boid_x_velocities,boid_y_velocities)
   scatter.set_offsets(zip(boids_x,boids_y))


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
