#!/usr/bin/env python
#
# $Id: amps-table.py 68 2014-02-18 23:49:56Z nicb $
#
import AmpiezzeDB

adb = AmpiezzeDB.AmpiezzeDB("../data/ampiezze.data")

frqbins = ((60, 120), (204, 408), (693, 1388), (2358, 4717))
nominal = (50, 45, 40, 30)

print "--------+--------------+---------------+---------------+---------------+"
header = "amp.nom.| "
for i in range(len(frqbins)):
	low = frqbins[i][0]
	hi  = frqbins[i][1]
	header = "%s%-4d    %-4d |  " % (header,low,hi)

print header
print "--------+--------------+---------------+---------------+---------------+"

for i in range(len(nominal)):
	nom = nominal[i]
	output = "    %02d  | " % nom
	
	for j in range(len(frqbins)):
		low = frqbins[j][0]
		hi  = frqbins[j][1]
		output = "%s%4.1f -> %4.1f |  " % (output, adb.amp(nom, low), adb.amp(nom, hi))

	print output
	print "--------+--------------+---------------+---------------+---------------+"
