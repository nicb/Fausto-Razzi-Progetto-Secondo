#!/usr/bin/env python
#
# $Id: pIIPicA0.py 68 2014-02-18 23:49:56Z nicb $
#
import RendererPicA0
import sys


r = RendererPicA0.RendererPicA0()

argc = len(sys.argv)

if argc > 1:
	n = 1
	while n < argc:
		mod = sys.argv[n]
		r.render_single(mod)
		n = n+1
else:
	r.render_all()
