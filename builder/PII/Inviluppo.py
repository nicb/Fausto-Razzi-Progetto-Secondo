#
# $Id: Inviluppo.py 68 2014-02-18 23:49:56Z nicb $
#
from string import split,atof
import Modulo

import pdb

class EnvValue:

	def __init__(self, vals):
		self.values = []
		values = split(vals,",")
		for i in range(len(values)):
			self.values.append(atof(values[i]))

class Inviluppo:
	"""Inviluppo -- classe degli inviluppi

	   proprieta`:
	   - amp: ampiezza nominale di riferimento
	   - instr: strumento csound da utilizzare
	   - values: oggetto EnvValue (che contiene i p-fields da passare a Csound)
	"""

	def __init__(self, idx, amp, instr, values):
		self.idx = idx
		self.amp = amp
		self.instr = instr
		self.pfields = EnvValue(values)

class ModReference:
	"""Inviluppo -- classe degli inviluppi

	   proprieta`:
	   - start: inizio validita` temporale dell'inviluppo
	   - end: fine validita` temporale dell'inviluppo
	   - inviluppo: inviluppo di riferimento
	"""

	def __init__(self, inv, start = 0, end = Modulo.Modulo.tfin):
		#pdb.set_trace()
		self.inviluppo = inv
		self.start = start
		self.end = end

