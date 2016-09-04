#!/usr/bin/env python
#
# $Id: envs-test.py 68 2014-02-18 23:49:56Z nicb $
#

import InviluppiDB

import pdb

idb = InviluppiDB.InviluppiDB()

testbed = { '14a': [ 50, 200, 300, 400, 550, 800 ],\
			'14b': [ 300, 600 ],\
			'05': [ 300, 600 ],\
			'10': [ 300, 600 ],\
		  }

print "we have %d envelopes" % len(idb.db)

keys = testbed.keys()
keys.sort()
for k in keys:
	for i in range(len(testbed[k])): 
		inv = idb.inviluppo(k, testbed[k][i])
		vals = ""
		for j in range(len(inv.pfields.values)):
			vals = "%s%-3.2f " % (vals, inv.pfields.values[j])
		print "Mod %s@%-4d: instr=%d, amp=%d, env values=%s" %\
			(k, testbed[k][i], inv.instr, inv.amp, vals)
