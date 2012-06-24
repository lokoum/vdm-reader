import urllib

class vdm:
	def __init__(self):
		try:
			self.page = urllib.urlopen("http://feeds.feedburner.com/viedemerde").read()
		except IOError:
			self.page = ''
	def new_story(self):
		'''The fastest and the recomended option'''
		start_quote = self.page.find("Aujourd'hui, ")
		end_quote = self.page.find(". VDM")+5
		vdm = self.page[start_quote:end_quote]
		self.page = self.page[end_quote:]
		if len(vdm) >= 310:
			return self.new_story()
		return vdm

	def random_story(self):
		'''This option is beta but useful if the feedburner page is already read'''
		'''Get a story from vdm'''
		chars_to_delete = ['</a><a href="', 'class="fmllink">', "/sante/'", "/sexe/", "/travail/", "/animaux/",
		"</a>", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "/inclassable/", "/amour/",
		 "/enfants/", "/argent/", '"', "?quot;"]
		page = urllib.urlopen("http://www.viedemerde.fr/aleatoire").read()
		story = (page[page.find('class="fmllink">')+16:page.find('" class="fmllink"> VDM</a>')+26])
		del page
		for x in chars_to_delete:
			story = story.replace(x, "")
		if (310 >= len(story)):
			return story
		return self.random_story()
