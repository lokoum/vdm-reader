import urllib

class vdm:
	def __init__(self):
		try:
			self.page = urllib.urlopen("http://feeds.feedburner.com/viedemerde").read()
		except IOError:
			self.page = ''
	def new_story(self):
		start_quote = self.page.find("Aujourd'hui, ")
		end_quote = self.page.find(". VDM")+1
		vdm = self.page[start_quote:end_quote]
		self.page = self.page[end_quote:]
		if len(vdm) >= 170:
			return self.new_story()
		elif vdm == '':
			return None
		return vdm
