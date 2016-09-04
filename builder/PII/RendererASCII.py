#
# $Id: RendererASCII.py 68 2014-02-18 23:49:56Z nicb $
#
import Modulo
import Renderer

class RendererASCII (Renderer.Renderer):

	def module_header(self, m):
		print "\nModulo: %s (Inizio: %9.4f, Fine: %9.4f)" % (m.tag, m.start, \
			m.start + m.dur)

	def render_module(self, m):
		for l in m.linee:
			start = l.start
			print "   L:%02d F:%8.3f (%3s: %+04.2f, %+04.2f), at:%9.4f d:%9.4f fine:%9.4f" % \
				(l.f.num, l.f.frequenza_base, l.f.ancillari.tag, \
				l.f.ancillari.a1, l.f.ancillari.a2, start, \
				l.dur, start+l.dur)
