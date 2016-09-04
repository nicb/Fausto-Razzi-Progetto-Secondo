#
# $Id: Linea14b.py 68 2014-02-18 23:49:56Z nicb $
#
import Linea14a
from Evento import Nota, Pausa

class Linea14b(Linea14a.Linea14a):
	"""Linea14b --- Oggetto Linea14b"""

	def fill(self, lf, lt):
		straight = Linea14a.Linea14a.fill(self, lf, lt)

		inverted = []

		# cross time information between subsequent notes and pauses
		# invert pauses and notes in the sequence
		# finish before the last note because it is going to be a pause
		# anyway
		for i in range(0, len(straight)-1, 2):
			n  = straight[i]
			p  = straight[i+1]
			nn = Nota(p.at, p.dur, n.frqs[0], n.frqs[1], n.frqs[2], n.amp)
			np = Pausa(n.at, n.dur)
			inverted.append(np)
			inverted.append(nn)
			

		del straight

		return inverted


	def __init__(self, lf, lt, stretch, endtime=240):
		Linea14a.Linea14a.__init__(self, lf, lt, stretch, endtime)
