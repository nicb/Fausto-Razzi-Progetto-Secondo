#
# $Id: Modulo14b.py 68 2014-02-18 23:49:56Z nicb $
#
"""Modulo14b --- Oggetto Modulo14b (Modulo specializzato)"""

import Modulo
import Modulo14a
import Linea14b

class Modulo14b (Modulo14a.Modulo14a):

	def set_linea(self, num, lf, lt):
		self.insert_linea(num, Linea14b.Linea14b(lf, lt, Modulo14a.Modulo14a.sfactor))

	def __init__(self, tag, endfactor = 0, end = Modulo.Modulo.tfin):
		Modulo14a.Modulo14a.__init__(self, tag, endfactor, end)
