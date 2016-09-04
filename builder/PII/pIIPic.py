#!/usr/bin/env python
#
# $Id: pIIPic.py 68 2014-02-18 23:49:56Z nicb $
#
import RendererPic
import sys


r = RendererPic.RendererPic()

argc = len(sys.argv)

if argc > 1:
	n = 1
	while n < argc:
		mod = sys.argv[n]
		r.render_single(mod)
		n = n+1
else:
	r.render_all()
