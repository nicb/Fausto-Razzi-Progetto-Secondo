#
# $Id: RendererCsound.py 68 2014-02-18 23:49:56Z nicb $
#
import Renderer
import InviluppiDB
import AmpiezzeDB
import GlobInv
import Modulo

import pdb

class RendererCsound (Renderer.Renderer):
	tablesize = 4096
	envtableoff = 10
	genvtableoff = 100
	genvtablefuzz = 0.3
	idb = InviluppiDB.InviluppiDB()
	adb = AmpiezzeDB.AmpiezzeDB()
	gim = { '01': 'B', '02': 'B', '03': 'B', '04': 'B', '05': 'B',\
			'06': 'B', '07': 'B', '08': 'B', '09': 'B', '10': 'C',\
			'11': 'C', '12': 'D', '13': 'D', '14a': 'A', '14b': 'A', }
	gimn = { 'A': 0, 'B': 1, 'C': 2, 'D': 3 }
	modidx = { '01': 1, '02': 2, '03': 3, '04': 4, '05': 5, '06': 6,\
	           '07': 7, '08': 8, '09': 9, '10': 10, '11': 11, '12': 12,\
	           '13': 13, '14a': 14, '14b': 15, }

	def genvelope_tables(self):
		#pdb.set_trace()
		keys = RendererCsound.gimn.keys()
		keys.sort()
		for k in keys:
			ginv = GlobInv.gi[k]
			coordstrings = "%5.2f " % ginv.segs[0][1]
			accu = 0
			for j in range(1, len(ginv.segs)):
				x = int((ginv.segs[j][0]/Modulo.Modulo.tfin) * RendererCsound.tablesize)-accu
				y = ginv.segs[j][1]
				coordstrings = "%s%d %6.3f " % (coordstrings, x, y)
				accu = accu+x
			print "f%d 0 %d 7 %s" % (RendererCsound.gimn[k]+RendererCsound.genvtableoff,\
				RendererCsound.tablesize+1, coordstrings)


	def genvelopes(self):
		for k in RendererCsound.gim.keys():
			gi = GlobInv.gi[RendererCsound.gim[k]]
			print "i10 0 %5.1f %d %d" % (Modulo.Modulo.tfin+\
			    RendererCsound.genvtablefuzz,\
				RendererCsound.gimn[RendererCsound.gim[k]]+\
				RendererCsound.genvtableoff,\
				RendererCsound.modidx[k])

	def module_header(self, m):
		print ";\n; Modulo %s - start: %9.4f end: %9.4f\n;" % \
			(m.tag, m.start, m.start + m.dur)

	def module_trailer(self, key):
		print ";================================================"

	def global_header(self):
		print ";\n; QUESTO FILE E` GENERATO AUTOMATICAMENTE - OGNI CAMBIAMENTO VERRA` SOVRASCRITTO\n;"
		print "; Fausto Razzi - Progetto II"
		print ";\nf1 0 8192 10 1\n;"
		self.genvelope_tables()
		self.genvelopes()

	def global_trailer(self):
		print "e\n; FINE"

	def output_nota(self, ms, e, n, m, l, tag):
		#pdb.set_trace()
		nmod = RendererCsound.modidx[m.tag]
		inv = RendererCsound.idb.inviluppo(m.tag, e.at)
		amp = RendererCsound.adb.amp(inv.amp, e.frqs[0])
		envs = ''
		for i in range(len(inv.pfields.values)):
			envs = "%s%4.2f " % (envs, inv.pfields.values[i])
		print "i%d %9.4f %9.4f %9.4f %9.4f %9.4f %9.4f %d %s; evento: %s" % \
			(inv.instr, ms+e.at, e.dur, amp, e.frqs[0], e.frqs[1], e.frqs[2],\
			 nmod, envs, tag)

	def output_pausa(self, ms, e, n, m, l, tag):
		print "; pausa %9.4f %9.4f (evento %s)" % (ms+e.at, e.dur, tag)

	def render_linea(self, m, l):
		print ";\n; Modulo %s Linea %2d - f0: %9.4f (%s: %s - %+5.2f, %+5.2f)\n;" % \
			(m.tag, l.f.num, l.f.frequenza_base, l.f.ancillari.index, l.f.ancillari.tag,\
			l.f.ancillari.a1, l.f.ancillari.a2)
		return Renderer.Renderer.render_linea(self, m, l)

	def render_module(self, m):
		if self.global_offset:
			print "a 0 0 %9.4f\n" % (self.global_offset)
		for i in m.linee:
			self.render_linea(m, i)
