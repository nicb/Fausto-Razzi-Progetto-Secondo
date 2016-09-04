#!/usr/bin/env python
#
# $Id: room_dbg.py 68 2014-02-18 23:49:56Z nicb $
#
# Room parameter checker and debugger for Progetto Secondo, version with room
# acoustics
#

import math
from sys import argv
import Gnuplot

def usage():
	print "Usage: %s <distance value>" % (argv[0])

class Size:

	def __init__(self, w, d):
		self.width = w
		self.depth = d

class Coord:

	def __init__(self, x, y):
		self.x = x
		self.y = y

class Vector:

	def plot(self):
		g = Gnuplot.Gnuplot(persist=1)
		d = Gnuplot.Data(self.data(), with='lines lw 6')
		g.plot(d)

	def xlength(self):
		return self.end.x-self.start.x

	def ylength(self):
		return self.end.y-self.start.y

	def length(self):
		return math.hypot(self.xlength(), self.ylength())
		
	def __add__(self, v):
		return Vector(self.start, Coord(self.xlength()+v.xlength(),\
				self.ylength()+v.ylength()))
		
	def __sub__(self, v):
		return Vector(self.start, Coord(self.xlength()-v.xlength(),\
				self.ylength()-v.ylength()))

	def __float__(self):
		return [[self.start.x, self.start.y],[self.end.x, self.end.y]]

	def __init__(self, start, end):
		self.start = start
		self.end   = end

def plot(data):
	d = Gnuplot.Data(data[0],with='lines lw 6')
	g = Gnuplot.Gnuplot(persist=1)
	g.plot(d)
	for i in data:
		d.append(i.data())
		g.replot(i)

class Source:
	speaker_y_guide = 3
	Listener = Coord(0, 0)
	Speakers = { 'left': Coord(-1.5, speaker_y_guide),\
				 'right': Coord(1.5, speaker_y_guide) }
	Room = Size(4, 50)
	front =  (Room.depth/2)-Speakers['left'].y
	back  = -(Room.depth/2)+Speakers['left'].y
	sspeed = 344


	def __init__(self, posx, posy):
		self.orig = Coord(posx, posy)
		self.r1l = Coord(-Room.width-self.orig.x,self.orig.y)
		self.r1r = Coord(Room.width-self.orig.x,self.orig.y)
		self.r1f = Coord(self.orig.x,Room.depth-self.orig.y)
		self.r1b = Coord(self.orig.x,-Room.depth-self.orig.y)

