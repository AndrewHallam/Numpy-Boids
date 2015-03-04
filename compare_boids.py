# Comparison of the three different implementations of boids.
import numpy as np
import random
import timeit
from class_boid import boid 
from update_boids import update_boids as object_update


setup_bad='''from bad_boids import update_boids
import random

boids_x=[random.uniform(-450,50.0) for x in range(50)]
boids_y=[random.uniform(300.0,600.0) for x in range(50)]
boid_x_velocities=[random.uniform(0,10.0) for x in range(50)]
boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(50)]
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)
'''

setup_object='''from class_boid import boid 
from update_boids import update_boids

import random

boids_x=[random.uniform(-450,50.0) for x in range(50)]
boids_y=[random.uniform(300.0,600.0) for x in range(50)]
boid_x_velocities=[random.uniform(0,10.0) for x in range(50)]
boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(50)]

boids=[boid(boids_x[i],boids_y[i],boid_x_velocities[i], boid_y_velocities[i]) for i in range(50)]
'''
setup_fast='''from fast_boids import update_boids
import random
import numpy as np

fast_x=np.array([random.uniform(-450,50.0) for x in range(50)])
fast_y=np.array([random.uniform(300.0,600.0) for x in range(50)])
fast_xv=np.array([random.uniform(0,10.0) for x in range(50)])
fast_yv=np.array([random.uniform(-20.0,20.0) for x in range(50)])
'''

time_bad_update=timeit.timeit('update_boids(boids)', setup_bad, number=200)
time_object_update=timeit.timeit('update_boids(boids)',setup_object, number=200)
time_fast_update=timeit.timeit('update_boids(fast_x,fast_y,fast_xv,fast_yv)', setup_fast, number=200)

print time_bad_update
print time_object_update
print time_fast_update
