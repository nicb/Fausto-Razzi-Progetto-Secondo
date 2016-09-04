#
# $Id: Ampiezza.py 68 2014-02-18 23:49:56Z nicb $
#
from string import atoi

class Ampiezza:
	"""Ampiezza --- Oggetto Ampiezza"""
	frqs = (60, 120, 204, 408, 693, 1388, 2358, 4717)

	def map(self, frq):
		"""Ampiezza.map

		   - trova la zona di frequenze in cui si colloca la frequenza
		     data in argomento
		   - interpola linearmente l'ampiezza per la frequenza data
		"""
		low = 0
		hi  = 0

		for i in range(len(Ampiezza.frqs)-1):
			if frq >= Ampiezza.frqs[i] and frq <= Ampiezza.frqs[i+1]:
				low = Ampiezza.frqs[i]
				hi  = Ampiezza.frqs[i+1]
				break

		afact = (self.amps[i+1]-self.amps[i])/(hi-low)
		bfact = self.amps[i]-(afact*low)
		result = (afact*frq)+bfact

		return result


	def __init__(self, nominal, a1, a2, a3, a4, a5, a6, a7, a8):
		self.amp = nominal
		self.amps = [ a1, a2, a3, a4, a5, a6, a7, a8 ]
