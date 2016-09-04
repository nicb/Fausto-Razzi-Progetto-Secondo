#
# $Id: Linea14a.py 68 2014-02-18 23:49:56Z nicb $
#
import Linea

class Linea14a(Linea.Linea):
	"""Linea14a --- Oggetto Linea14a"""

	def fill(self, lf, lt):
		result = Linea.Linea.fill(self, lf, lt)

		for i in range(len(result)):
			result[i].stretch(self.stretch)

		self.start = self.start * self.stretch
		self.dur = self.dur * self.stretch

		return result


	def __init__(self, lf, lt, stretch, endtime=240):
		self.stretch = stretch
		Linea.Linea.__init__(self, lf, lt, endtime)
		self.endtime = endtime * stretch
