from lib.vdm import *

def main():
	while True:
		try:
			print("%s\n" % random_story())
			raw_input()
		except IOError:
			print("Erreur de connection :(")
	return 0
if __name__ == '__main__':
	main()
