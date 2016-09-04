#
# $Id: Modulo14a.py 68 2014-02-18 23:49:56Z nicb $
#
"""Modulo14a --- Oggetto Modulo14a (Modulo specializzato)"""

import Modulo
import Linea14a

class Modulo14a (Modulo.Modulo):
	sfactor = 3

	def set_linea(self, num, lf, lt):
		self.insert_linea(num, Linea14a.Linea14a(lf, lt, Modulo14a.sfactor))

	def __init__(self, tag, endfactor = 0, end = Modulo.Modulo.tfin):
		#endfactor = endfactor * Modulo14a.sfactor
		Modulo.Modulo.__init__(self, tag, endfactor, end)
		self.dur = self.dur * Modulo14a.sfactor
		self.start = end - self.dur;
