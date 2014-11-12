__author__ = 'Sherif'
import random
import os
import yaml
class boid (object):
    def __init__(self, px, py, vx, vy):
        config = yaml.load(open(os.path.join(os.path.dirname(__file__), 'initial_config.yml')))
        self.ran.boid= config["ran_boids"]
        self.fly_mid=config["fly_mid"]
        self.fly_away= config["fly_away"]
        self.speed_match= config ["speed_match"]
        self.speed_match2= config["speed_match2"]

        ## For each boid
        self.px=px
        self.py=py
        self.vx=vx
        self.vy=vy






