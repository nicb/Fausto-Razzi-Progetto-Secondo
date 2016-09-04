#
# $Id: Linea.py 68 2014-02-18 23:49:56Z nicb $
#
import string
import LineaFrequenza
import LineaTempo
from Evento import Nota, Pausa
import AmpiezzeDB

class Linea:
	"""Linea --- Oggetto Linea"""
	adb = AmpiezzeDB.AmpiezzeDB()
	nominalamp = 50

	def fill(self, lf, lt):
		result = []
		self.num = lt.num
		self.start = lt.start
		self.dur = lt.dur

		at = self.start
		i = 0;
		for i in range(lt.npause):
			n = Nota(at, lt.suoni[i], lf.f0(), lf.f1(), lf.f2(),\
				Linea.adb.amp(Linea.nominalamp, lf.f0()))
			result.append(n)
			at = at + lt.suoni[i]
			p = Pausa(at, lt.pause[i])
			result.append(p)
			at = at + lt.pause[i]
		else:
			n = Nota(at, lt.suoni[i], lf.f0(), lf.f1(), lf.f2(),\
				Linea.adb.amp(Linea.nominalamp, lf.f0()))
			result.append(n)

		return result

	def __init__(self, lf, lt, endtime=240):
		self.sequenza = self.fill(lf, lt)
		self.endtime = endtime
		self.f = lf		# this must be kept for reference
		del lt			# this can be deleted instead
