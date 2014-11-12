__author__ = 'Sherif'
import random
from numpy import array
import matplotlib.pyplot as plt
class boids (type):
    def __init__(self, boids_x, boids_y, boid_x_velocities, boid_y_velocities):
         self.boids_x=[random.uniform(-450,50.0) for x in range(50)]
         self.boids_y=[random.uniform(300.0,600.0) for x in range (50)]
         self.boid_x_velocities=[random.uniform(-20.0,20.0)for x in range(50)]
         self.boid_x_velocities=[boid_x_velocities for x in range(50)]
         boids = [boids(type) for type in boids_x, boids_y, boid_x_velocities, boid_y_velocities]

    def update_boids(boids):
        xs,ys,xvs,yvs=boids
        # Fly towards
    def velocity (self, xvs, yvs):
        for i in range(len(xs)):
            for j in range(len(xs)):
                self.xvs, self.yvs= xvs, yvs
    def change_velcoity (self, A, B):
        for i in range(len(xs)):
            for j in range(len(xs)):
                A=(xs[j]-xs[i])*0.01/len(xs)
                B=(ys[j]-ys[i])*0.01/len(xs)
            return change_velcoity(self.xvs[i]+A, yvs[i]+B)


        # Moving away
    def moving_away (self, xs, xy):
            self.xs=xs
            self.xy=xy
    def distance(self, xa, ya, xb, yb):
        return (xb-xa)**2 + (yb-ya)**2
    def compute_sum (self, xvs, yvs):
        for i in range(len(self.xs)):
            for j in range(len(self.xs)):
                if (self.distance(self.xs[i],self.ys[i], self.xs[j], self.ys[j])) < 100:
                    self.xvs[i]+= self.xs[i]-self.xs[j]
                    self.yvs[i]+= (self.ys[i]-self.ys[j])
# Speed match
    def speed_match (self, xvs, yvs):
        for i in range(len(self.xs)):
            for j in range(len(self.xs)):
                if (self.distance(self.xs[i],self.ys[i], self.xs[j], self.ys[j])) < 10000:
                    self.xvs[i]+=(self.xvs[j]-self.xvs[i])*0.125/len(self.xs)
# Move according to velocities
    def move(self, xs, ys, xvs, yvs):
        for i in range(len(self.xs)):
            self.xs[i]=self.xs[i]+self.xvs[i]
            self.ys[i]=self.ys[i]+self.yvs[i]





figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(boids[0],boids[1])
def animate(frame):
    update_boids(boids)
    scatter.set_offsets(zip(boids[0],boids[1]))
    anim = animation.FuncAnimation(figure, animate, frames=50, interval=50)
    if __name__ == "__main__":
        plt.show()
