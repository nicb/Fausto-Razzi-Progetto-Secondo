#
# InviluppiDB.py,v 0.1 2005/11/05 03:38:17 nicb Exp
#
from string import atoi, atof, split
from ConfParser import LineParser
import Inviluppo
import Modulo
import copy

import pdb


class InviluppiDB (LineParser.LineParser):
	db = []
	mod_ref = {}

	def inviluppo(self, modulo, time):
		modrefs = InviluppiDB.mod_ref[modulo]
		for i in range(len(modrefs)):
			if time >= modrefs[i].start and time < modrefs[i].end:
				break
		return modrefs[i].inviluppo

	def parse_modules(self, modulefield):
		modparts = split(modulefield,"(")
		modulo = modparts[0]
		if len(modparts) > 1:
			timings = split(modparts[1],",")
			start = atof(timings[0])
			end = atof(timings[1][0:-1])
		else:
			start = 0
			end = Modulo.Modulo.tfin

		return (modulo, start, end)

	def save(self, r):
		"""InviluppiDB.save(record)

		formato record:
		- indice dell'inviluppo
		- moduli e validita` di tempo (mod[(start,end)],...)
		- strumento num
		- segmenti (x0,y0;x1,y1...)
		"""
		#pdb.set_trace()
		idx = atoi(r[0])
		I = Inviluppo.Inviluppo(idx, atoi(r[2]), atoi(r[3]), r[4])
		InviluppiDB.db.insert(idx-1,I)
		moduli = split(r[1],":")
		for m in moduli:
			(modulo, start, end) = self.parse_modules(m)
			mr = Inviluppo.ModReference(I, start, end)
			if InviluppiDB.mod_ref.has_key(modulo):
				InviluppiDB.mod_ref[modulo].append(mr)
			else:
				InviluppiDB.mod_ref[modulo] = [ mr ]

	def __init__(self, fdbname="data/inviluppi.data"):
		LineParser.LineParser.__init__(self)
		self.load(fdbname)
