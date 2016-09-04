#
# $Id: Modulo.py 68 2014-02-18 23:49:56Z nicb $
#
"""Modulo --- Oggetto Modulo"""

import Linea

class Modulo:
	dur  = 240
	tfin = 720

	def apply_endfactor(self, lt):
		lt.start = lt.start - (self.endfactor*(lt.num-1))

	def insert_linea(self, num, l):
		self.linee.insert(num-1, l)

	def set_linea(self, num, lf, lt):
		self.insert_linea(num, Linea.Linea(lf, lt))

	def __init__(self, tag, endfactor = 0, end = tfin):
		self.tag = tag;
		self.endfactor = endfactor;
		self.dur = Modulo.dur;
		self.start = end - self.dur;
		self.linee = [];
