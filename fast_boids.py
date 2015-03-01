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
    
        
        for i in range(xs.size):
                for j in range(xs.size):
                       distance=(xs[j]-xs[i])**2 + (ys[j]-ys[i])**2
                       
                       if distance < 100:
                              xvs[i]+=(xs[i]-xs[j])+(xs[j]-xs[i])*0.01/len(xs)
			      yvs[i]+=(ys[i]-ys[j])+(ys[j]-ys[i])*0.01/len(xs)
                              
                       else:
                              xvs[i]+=(xs[j]-xs[i])*0.01/len(xs)
			      yvs[i]+=(ys[j]-ys[i])*0.01/len(xs)
       
        for i in range(xs.size):
                for j in range(xs.size):
                       distance=(xs[j]-xs[i])**2 + (ys[j]-ys[i])**2
                       if distance < 10000:
                              xvs[i]+=(xvs[j]-xvs[i])*0.125/len(xs)
			      yvs[i]+=(yvs[j]-yvs[i])*0.125/len(xs)
                              
		xs += xvs
		ys += yvs


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
