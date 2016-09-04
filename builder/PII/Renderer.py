#
# $Id: Renderer.py 68 2014-02-18 23:49:56Z nicb $
#
import ModuliDB

class Renderer:

	def __init__(self):
		self.mdb = ModuliDB.ModuliDB()

	def global_header(self):
		pass

	def global_trailer(self):
		pass

	def module_header(self, m):
		pass

	def module_trailer(self, m):
		pass

	def event_tag(self, n, m, l):
		return "%3s-%02d-%02d" % (m.tag, l.num, (n/2)+1)

	def output_nota(self, ms, e, n, m, l, tag):
		pass

	def output_pausa(self, ms, e, n, m, l, tag):
		pass

	def output_event(self, ms, e, n, m, l):
		tag = self.event_tag(n, m, l)
		if e.is_a == 'nota':
			self.output_nota(ms, e, n, m, l, tag)
		elif e.is_a == 'pausa':
			self.output_pausa(ms, e, n, m, l, tag)

	def render_linea(self, m, l):
		for i in range(len(l.sequenza)):
			self.output_event(m.start, l.sequenza[i],i,m,l)
		return m.start

	def render_module(self, m):
		pass

	def render(self, key):
		m = self.mdb.get(key)	
		self.module_header(m)
		self.render_module(m)
		self.module_trailer(m)

	def render_all(self):
		self.global_offset = 0
		self.global_header()

		keys = self.mdb.db.keys()
		keys.sort()

		for k in keys:
			self.render(k)

		self.global_trailer()

	def render_single(self, key):
		self.global_offset = self.mdb.get(key).start
		self.global_header()
		self.render(key)
		self.global_trailer()
