
from room_dbg import Vector,Coord,plot
import Gnuplot

v1 = Vector(Coord(0,0),Coord(5,9))
v2 = Vector(Coord(0,0),Coord(5,-9))
v3 = v1 + v2

plot([v1, v2, v3])

