from vpython import *

class stellar:
    #lumin- luminousity,rad-radius,mas-mass,st-surface temperature,t-time
    def __init__(self,lumin,rad,mas,t,st):
        self.lumin=lumin
        self.rad=rad
        self.mas=mas
        self.t=t
        self.st=st
    def star(self):
        scene=canvas()
        scene.autoscale = False
        sphere(pos=vector(0,0,0),texture="https://i.imgur.com/1nVWbbd.jpg",radius=self.rad,shininess=self.lumin)
        b = sphere(color=color.white,opacity=100)
        b
    
star1=stellar(100,25,300,5,300)
star1.star()
