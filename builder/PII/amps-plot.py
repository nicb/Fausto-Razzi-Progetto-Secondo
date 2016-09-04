#!/usr/bin/env python
#
# $Id: amps-plot.py 68 2014-02-18 23:49:56Z nicb $
#
import AmpiezzeDB

adb = AmpiezzeDB.AmpiezzeDB()

amps = ((60, 120), (204, 408), (693, 1388), (2358, 4717))

print "set term postscript color"
print "set logscale x"
print "plot [50:5000][20:70] '-' using 1:2 title 'Nom: 50 dB' w lines lw 6,\
	  '-' using 1:3 title 'Nom: 40 dB' w lines lw 6,\
	  '-' using 1:4 title 'Nom: 30 dB' w lines lw 6"

for i in range(3):
	for i in range(len(amps)):
		low = amps[i][0]
		hi  = amps[i][1]
		j = low
	
		while j < hi: 
			print "%f %f %f %f" % (j, adb.amp(50, j), adb.amp(40, j), adb.amp(30, j))
			j = j + 0.5
	
		print "\n"
	print "e"
