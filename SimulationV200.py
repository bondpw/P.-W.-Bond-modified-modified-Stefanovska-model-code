from SimulationV400_Process import Process as pro 
from DefUpdateV200 import update as up
import math as ma

situation = up(0.5,0.5,0.5,0.5,0.5,0.5,0.5,1,1,1,1,1,2.2*ma.pi,0.46*ma.pi,0.2*ma.pi,0.5,-0.5,0.3,0)
forward = pro(0.01,25000,situation,15,10,0)
forward.movementvarkappa()