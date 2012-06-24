from lib.vdm import *

def main():
	x = vdm()
	while True:
		try:
			s = x.new_story()
			if s != '':
				print("%s\n" % s)
			else:
				print("%s\n" % x.random_story())
			raw_input()
		except IOError:
			print("Erreur de connection :(")
	return 0
if __name__ == '__main__':
	main()
