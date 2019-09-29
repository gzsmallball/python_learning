from html.parser import HTMLParser

class URLLister(HTMLParser):
	def reset(self):
		HTMLParser.reset(self)
		self.urls = []
	
	def start_a(self,attrs):
		href = [v for k,v in attrs if k == 'href']
		if href:
			self.urls.extend(href)
	