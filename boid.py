__author__ = 'Sherif'
import random
import os
import yaml
class boid (object):
    def __init__(self, px, py, vx, vy):
        config = yaml.load(open(os.path.join(os.path.dirname(__file__), 'initial_config.yml')))
        self.ran.boid= config["ran_boids"]




