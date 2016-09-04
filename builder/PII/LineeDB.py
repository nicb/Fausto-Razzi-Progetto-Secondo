#
# $Id: LineeDB.py 68 2014-02-18 23:49:56Z nicb $
#
import string
from ConfParser import LineParser
import LineaTempo
import copy


class LineeDB (LineParser.LineParser):
	nlinee = 13

	def linea(self, idx):
		return copy.deepcopy(self.db[idx-1])

	def save(self, record):
		idx = string.atoi(record[0])
		l = LineaTempo.LineaTempo(idx, string.atof(record[1]), string.atoi(record[2]), string.atof(record[3]))
		self.db[idx-1] = l

	def __init__(self, fdbname="data/linee.data"):
		LineParser.LineParser.__init__(self)
		self.db = [None] * LineeDB.nlinee
		self.load(fdbname)
