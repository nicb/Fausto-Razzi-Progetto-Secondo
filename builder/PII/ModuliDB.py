#
# $Id: ModuliDB.py 68 2014-02-18 23:49:56Z nicb $
#
import string
from ConfParser import LineParser
import Modulo
import Modulo14a
import Modulo14b
import LineaFrequenza
import AncillariDB
import LineeDB

def reverse_sort(a, b):
	if (a < b):
		return 1
	elif (b < a):
		return -1
	else:
		return 0

class ModuliDB (LineParser.LineParser):
	db = { '01': None, '02': None, '03': None, '04': None, '05': None, '06': None, '07': None, '08': None, '09': None, '10': None, '11': None, '12': None, '13': None, '14a': None, '14b': None};
	ldb = LineeDB.LineeDB()
	l_off = 0.75
	#kfact = 6.1538
	kfact = 6.153846

	def get(self, k):
		if '14' in k:
			result = k
		else:					# make sure it has a leading zero
			result = "%02d" % string.atoi(k)	

		return ModuliDB.db[result]


	def save(self, record):
		modulo = self.db[record[0]]
		nline = string.atoi(record[1]);
		lf = LineaFrequenza.LineaFrequenza(record[0], nline, string.atof(record[2]), record[3]);
		lt = ModuliDB.ldb.linea(nline)
		modulo.apply_endfactor(lt)
		modulo.set_linea(nline, lf, lt)

	def __init__(self, fdbname="data/frequenze.data"):
		LineParser.LineParser.__init__(self)
		keys = self.db.keys()
		keys.sort(reverse_sort)
		end = Modulo.Modulo.tfin

		for k in keys:
			nmod = string.atoi(k[0:2])
			if '14' in k:
				nmod = 7 # Modulo 14 uses Modulo 7 as a template
			endfactor = (13 - nmod) * ModuliDB.l_off
			if '14a' in k:
				self.db[k] = Modulo14a.Modulo14a(k, endfactor)
			elif '14b' in k:
				self.db[k] = Modulo14b.Modulo14b(k, endfactor)
			else:
				end = end - ((13 - nmod)*ModuliDB.kfact) 
				self.db[k] = Modulo.Modulo(k, endfactor, end)

		self.load(fdbname)
