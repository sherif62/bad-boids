__author__ = 'Sherif'

class boids (type):
    def __init__(self, boids_x, boids_y, boid_x_velocities, boid_y_velocities):
        from random import random
        for x in range (50):
        self.boids_x=random.uniform(-450,50.0)
        self.boids_y=random.uniform(300.0,600.0)
        self.boid_x_velocities=random.uniform(-20.0,20.0)
        self.boid_x_velocities=boid_x_velocities
        boids = [boids(type) for type in boids_x, boids_y, boid_x_velocities, boid_y_velocities

    def update_boids(boids):
        xs,ys,xvs,yvs=boids

       

























figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
   update_boids(boids)
   scatter.set_offsets(zip(boids[0],boids[1]))


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()








