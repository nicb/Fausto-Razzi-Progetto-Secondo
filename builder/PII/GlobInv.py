#
# $Id: GlobInv.py 68 2014-02-18 23:49:56Z nicb $
#

class GlobInv:

	def __init__(self, t0, y0, t1, y1, t2, y2, t3, y3, t4, y4, t5, y5):
		self.segs = [ (t0, y0), (t1, y1), (t2, y2), (t3, y3), (t4, y4),\
					  (t5, y5) ]


gi = { 'A': GlobInv(0, 0.5, 360.0, 0.125, 361.0, 1, 520.0, 0.128, 712.5, 1, 720.0, 0),\
	   'B': GlobInv(0, 0.7, 300.0, 1, 319.0, 0.7, 466.5, 0.7, 712.5, 0.7, 720.0, 0.7),\
	   'C': GlobInv(0, 0, 300.0, 0, 442.0, 0, 443.0, 0.7, 712.5, 1, 720.0, 0),\
	   'D': GlobInv(0, 0, 300.0, 0, 472.0, 0, 473.0, 0.7, 712.5, 1, 720.0, 0),\
	 }