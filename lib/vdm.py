import urllib

def random_story():
	'''Get a story from vdm'''
	chars_to_delete = ['</a><a href="', 'class="fmllink">', "/sante/'", "/sexe/", "/travail/", "/animaux/",
	"</a>", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "/inclassable/", "/amour/",
	 "/enfants/", "/argent/", '"', "?quot;"]
	page = urllib.urlopen("http://www.viedemerde.fr/aleatoire").read()
	story = (page[page.find('class="fmllink">')+16:page.find('" class="fmllink"> VDM</a>')+26])
	del page
	for x in chars_to_delete:
		story = story.replace(x, "")
	if (350 >= len(story)):
		return story
	return random_story()
