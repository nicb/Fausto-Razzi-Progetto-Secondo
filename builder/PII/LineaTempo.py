#
# $Id: LineaTempo.py 68 2014-02-18 23:49:56Z nicb $
#
"""LineaTempo --- Oggetto LineaTempo: informazione di Tempo della linea"""
import string

class LineaTempo:
	dur_modulo = 240

	def __init__(self, num, sound_dur, nsounds, minpause):
		self.num = num
		self.nsounds = nsounds
		self.suoni = [sound_dur] * self.nsounds
		self.npause  = nsounds - 1
		self.pause = [0] * self.npause
		self.minpause = minpause

		i = self.npause
		n = 0
		dur_pause = 0
		dur_suoni = 0
		while i:
			self.pause[n] = i * self.minpause
			dur_pause = dur_pause + self.pause[n]
			dur_suoni = dur_suoni + self.suoni[n]
			i = i - 1
			n = n + 1
		dur_suoni = dur_suoni + self.suoni[n]

		self.dur = dur_suoni + dur_pause
		self.start = LineaTempo.dur_modulo - self.dur
