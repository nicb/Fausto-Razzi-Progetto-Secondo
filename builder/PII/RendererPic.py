#
# $Id: RendererPic.py 68 2014-02-18 23:49:56Z nicb $
#
import Renderer

class RendererPic (Renderer.Renderer):

	def module_header(self, m):
		dur = m.start + m.dur
		print ".PS"
		print "#\n# Modulo %s - start: %9.4f end: %9.4f\n#" % \
			(m.tag, m.start, dur)
		print "Modulo(%s,%f,%f)" % (m.tag, m.start, dur)

	def module_trailer(self, key):
		print "#================================================"
		print ".PE"

	def global_header(self):
		print '.\\"\n.\\" QUESTO FILE E` GENERATO AUTOMATICAMENTE - OGNI CAMBIAMENTO VERRA` SOVRASCRITTO\n.\\"'
		print '.\\" Fausto Razzi - Progetto II\n.\\"'
		print '.PS\ncopy "PII.macros"\n.PE'

	def global_trailer(self):
		print '.\\" End of Pic Score'

	def output_nota(self, ms, e, n, m, l, tag):
		print "Linea(%s,%d,%f,%f,%f,%f,%f,%f) # evento %s" %\
			(m.tag, l.num, ms+e.at, e.dur, e.amp, e.frqs[0], e.frqs[1], e.frqs[2], tag)

	def output_pausa(self, ms, e, n, m, l, tag):
		tag = self.event_tag(n, m, l)
		print "# pausa %9.4f %9.4f (evento %s)" % (ms+e.at, e.dur, tag)

	def render_linea(self, m, l):
		print "#\n# Modulo %s Linea %2d - f0: %9.4f (%s: %s - %+5.2f, %+5.2f)\n#" % \
			(m.tag, l.f.num, l.f.frequenza_base, l.f.ancillari.index, l.f.ancillari.tag,\
			l.f.ancillari.a1, l.f.ancillari.a2)
		module_start = Renderer.Renderer.render_linea(self, m, l)
		print "Vertical_Correspondence(%s,%d)" % (m.tag, l.f.num)
		return module_start

	def render_module(self, m):
		for i in m.linee:
			self.render_linea(m, i)
