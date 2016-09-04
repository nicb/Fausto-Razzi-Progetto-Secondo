#
# $Id: RendererPicA0.py 68 2014-02-18 23:49:56Z nicb $
#
import string
import RendererPic

class RendererPicA0 (RendererPic.RendererPic):

	colors = ( 'green', 'blue', 'grey90', 'magenta', 'cyan', 'paleblue3', 'turquoise3', 'red', 'azure3', 'rosybrown3', 'chocolate3', 'darkolivegreen3', 'khaki3', 'bisque3', 'mistyrose3', 'darkviolet' )

	def module_header(self, m):
		dur = m.start + m.dur
		print "#\n# Modulo %s - start: %9.4f end: %9.4f\n#" % \
			(m.tag, m.start, dur)

	def module_trailer(self, key):
		print "#================================================"

	def global_header(self):
		print '.\\"\n.\\" QUESTO FILE E` GENERATO AUTOMATICAMENTE - OGNI CAMBIAMENTO VERRA` SOVRASCRITTO\n.\\"'
		print '.\\" Fausto Razzi - Progetto II\n.\\"'
		print '.PS\ncopy "PII-A0.macros"\n.PE'
		print ".PS"
		print "Score()"

	def global_trailer(self):
		print ".PE"
		print '.\\" End of Pic Score'

	def output_nota(self, ms, e, n, m, l, tag):
		col_number = string.atoi(m.tag[0:2])-1
		color = self.colors[col_number]
		print "Linea(%s,%d,%f,%f,%f,%f,%f,%f,\"%s\") # evento %s" %\
			(m.tag, l.num, ms+e.at, e.dur, e.amp, e.frqs[0], e.frqs[1], e.frqs[2], color, tag)

	def output_pausa(self, ms, e, n, m, l, tag):
		tag = self.event_tag(n, m, l)
		print "# pausa %9.4f %9.4f (evento %s)" % (ms+e.at, e.dur, tag)

#	def render_linea(self, m, l):
#		print "#\n# Modulo %s Linea %2d - f0: %9.4f (%s: %s - %+5.2f, %+5.2f) colore: \"%s\"\n#" % \
#			(m.tag, l.f.num, l.f.frequenza_base, l.f.ancillari.index, l.f.ancillari.tag,\
#			l.f.ancillari.a1, l.f.ancillari.a2, color)
#		module_start = RendererPic.RendererPic.render_linea(self, m, l)
#		print "Vertical_Correspondence(%s,%d)" % (m.tag, l.f.num)
#		return module_start

#	def render_module(self, m, color):
#		for i in m.linee:
#			self.render_linea(m, i, color)
#
#	def render(self, m, color)
#		m = self.mdb.get(key)	
#		self.module_header(m)
#		self.render_module(m, color)
#		self.module_trailer(m)
#
#
#	def render_all(self):
#		self.global_offset = 0
#		self.global_header()
#
#		keys = self.mdb.db.keys()
#		keys.sort()
#		n = 0
#
#		for k in keys:
#			self.render(k, colors[n])
#			n += 1
#
#		self.global_trailer()
