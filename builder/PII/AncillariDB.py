#
# $Id: AncillariDB.py 68 2014-02-18 23:49:56Z nicb $
#
from ConfParser import LineParser
import Ancillari
import string

class AncillariDB (LineParser.LineParser):
	octave_start = 60;
	octave_distance = 3.4;
	percentages = \
	[
		{ 'F': 1, 'E': 0.8, 'D': 0.6, 'C': 0.4, 'B': 0.2, 'G': -0.1, 'H': -0.3, 'I': -0.5, 'L': -0.7, 'M': -0.9 },
		{ 'F': 1, 'E': 0.8, 'D': 0.6, 'C': 0.4, 'B': 0.2, 'G': -0.1, 'H': -0.3, 'I': -0.5, 'L': -0.7, 'M': -0.9 },
		{ 'F': 1, 'E': 0.8, 'D': 0.6, 'C': 0.4, 'B': 0.2, 'G': -0.1, 'H': -0.3, 'I': -0.5, 'L': -0.7, 'M': -0.9 },
		{ 'F': 0.1, 'E': 0.08, 'D': 0.06, 'C': 0.04, 'B': 0.02, 'G': -0.01, 'H': -0.03, 'I': -0.05, 'L': -0.07, 'M': -0.09 },
	];

	def get_octave(self, freq):
		eps = 0.00001
		o = 0
		ob = AncillariDB.octave_start

		if (freq == 542.86): # median module
			return 3

		while o < 4:
			ot = ob * 2
			if (freq >= (ob-eps) and freq <= (ot+eps)):
				return o
			o = o + 1
			ob = ob * AncillariDB.octave_distance

		print "Warning: freq %8.3f did not fit!!" % freq
		return (o-1)

	def get_key(self, tag):
		return string.atoi(tag[1:])-1 # skipping the 'C' and getting the index
		                              # and making it zero-offset
		
	def ancillari(self, freq, tag):
		idx = self.get_key(tag)
		octave = self.get_octave(freq)
		key = self.db[idx]
		a1 = self.percentages[octave][key[1]] # second letter
		a2 = self.percentages[octave][key[2]] # third letter
		return Ancillari.Ancillari(tag, key, a1, a2)

	def save(self, record):
		idx = self.get_key(record[0])
		self.db.insert(idx,record[1]);

	def __init__(self, dbname="data/ancillari.data"):
		LineParser.LineParser.__init__(self)
		self.db = []
		self.load(dbname)
