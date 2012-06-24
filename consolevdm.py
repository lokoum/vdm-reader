from lib.vdm import *

def main():
	x = vdm()
	while True:
		try:
			print("%s\n" % x.new_story())
			raw_input()
		except IOError:
			print("Erreur de connection :(")
	return 0
if __name__ == '__main__':
	main()
