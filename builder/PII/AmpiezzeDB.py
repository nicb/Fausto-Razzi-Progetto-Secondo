#
# $Id: AmpiezzeDB.py 68 2014-02-18 23:49:56Z nicb $
#
from string import atof
from ConfParser import LineParser
import Ampiezza
import copy


class AmpiezzeDB (LineParser.LineParser):

	def amp(self, namp, frq):
		return self.db[str(namp)].map(frq)

	def save(self, r):
		key = r[0]
		a = Ampiezza.Ampiezza(atof(r[0]),atof(r[1]),atof(r[2]),atof(r[3]),\
						atof(r[4]),atof(r[5]),atof(r[6]),atof(r[7]),atof(r[8]))
		self.db[key] = a

	def __init__(self, fdbname="data/ampiezze.data"):
		LineParser.LineParser.__init__(self)
		self.db = {}
		self.load(fdbname)
