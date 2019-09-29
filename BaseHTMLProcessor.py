from html.parser import HTMLParser
import html.entities

class BaseHTMLProcessor(HTMLParser):
	def reset(self):
		self.pieces = []
		HTMLParser.reset(self)
	
	def unknow_starttag(self,tag,attrs):
		strattrs = "".join(["%s=%s" %(key,value) for key,value in attrs])
		self.pieces.append("<%(tag)s%(strattrs)s>" % locals() )
	
	def unknow_endtag(self,tag):
		self.pieces.append("</%(tag)s>" % locals())
	
	def handle_charref(self,ref):
		self.pieces.append("&#%(ref)s;" % locals())
	
	def handle_entityref(self,ref):
		self.pieces.append("&%(ref)s" % locals())
		if html.entities.entitydefs.has_key(ref):
			self.pieces.append(";")
	
	def handle_data(self,text):
		self.pieces.append(text)
	
	def handle_comment(self,text):
		self.pieces.append("<!-%(text)s->" % locals())
	
	def handle_pi(pi,text):
		self.pieces.append("<?%(text)s>" % locals())
	
	def handle_decl(self,text):
		self.pieces.append("<!%(text)s>" % locals())
	
	def output(self):
		"""return processd HTML as a single string"""
		return "\n".join(self.pieces)



