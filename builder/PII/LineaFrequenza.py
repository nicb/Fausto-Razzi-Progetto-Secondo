#
# $Id: LineaFrequenza.py 68 2014-02-18 23:49:56Z nicb $
#
"""LineaFrequenza --- Oggetto LineaFrequenza"""
import string
import Ancillari
import AncillariDB

class LineaFrequenza:
	adb = AncillariDB.AncillariDB();
	
	def f0(self):
		return self.frequenza_base

	def f_anc(self, a):
		return (self.frequenza_base*(1+(a/100)))

	def f1(self):
		return self.f_anc(self.ancillari.a1)

	def f2(self):
		return self.f_anc(self.ancillari.a2)

	def __init__(self, modulo, num, f0, atag):

		modnum = string.atoi(modulo[0:1]) # without the 'a' or 'b'

		self.modulo = modulo
		self.num = num
		self.frequenza_base = f0
		self.ancillari = LineaFrequenza.adb.ancillari(f0, atag)
