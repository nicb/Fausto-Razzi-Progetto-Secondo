#
# $Id: Evento.py 68 2014-02-18 23:49:56Z nicb $
#

class Evento:
	"""Evento

	classe di Eventi che hanno un action time ed una durata
	"""
	def stretch(self, sfactor):
		self.at = self.at * sfactor
		self.dur = self.dur * sfactor

	def __init__(self, is_a, at = 0, dur = 0):
		self.is_a = is_a
		self.at = at
		self.dur = dur

class Nota(Evento):

	def __init__(self, at = 0, dur = 0, frq0 = 0, frq1 = 0, frq2 = 0, amp = 50):
		Evento.__init__(self, 'nota', at, dur)
		self.frqs = [ frq0, frq1, frq2 ]
		self.amp = amp

class Pausa(Evento):

	def __init__(self, at = 0, dur = 0):
		Evento.__init__(self, 'pausa', at, dur)
