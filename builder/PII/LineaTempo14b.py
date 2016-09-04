#
# $Id: LineaTempo14b.py 68 2014-02-18 23:49:56Z nicb $
#
"""LineaTempo14b --- Oggetto LineaTempo14b: informazione di Tempo della linea 14b"""
import string
import LineaTempo
import Modulo14a

class LineaTempo14b(LineaTempo.LineaTempo):
	dur_modulo = LineaTempo.LineaTempo.dur_modulo * Modulo14a.Modulo14a.sfactor

	def __init__(self, lt):
		"""LineaTempo14b(line)

		accepts a LineaTempo line and re-threads durations and sounds
		completely (they need to be inverted)
		"""
		self.num = lt.num
		self.npause = lt.nsounds
		self.nsounds = lt.npause
		self.pause = lt.suoni
		self.suoni = [0] * self.nsounds
		self.mindur = lt.minpause

		i = self.nsounds
		n = 0
		dur_pause = 0
		dur_suoni = 0
		while i:
			self.suoni[n] = i * self.mindur
			dur_pause = dur_pause + self.pause[n]
			dur_suoni = dur_suoni + self.suoni[n]
			i = i - 1
			n = n + 1
		#dur_suoni = dur_suoni + self.suoni[n]

		self.dur = dur_suoni + dur_pause
		self.start = LineaTempo14b.dur_modulo - self.dur + self.pause[0]
		del lt
