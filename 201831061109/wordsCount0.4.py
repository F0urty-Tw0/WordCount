# coding=utf-8
import re
import sys
import getopt

from word_operate import word_operate

number = 10
isSave = False
outfile = ''


def main(argv):
	global number
	global isSave, outfile
	filename = ""
	contents = ""
	try:
		opts, args = getopt.getopt(argv, "m:n:i:o:")
	except getopt.GetoptError:
		print ('test.py -i <filepath> -m <number_of_phrase> -n <number_of_words> -o <outfile_path>')
	for opt, arg in opts:
		if opt == '-i':
			filename = arg
		elif opt == '-n':
			if arg.isdigit():
				number = int(arg)
			elif arg.isalpha():
				print("-n para is integer!")
				sys.exit(1)
		elif opt == '-o':
			isSave = True
			outfile = arg
		
	if filename == '':
		print("Please at least enter the '-i' parameter!")
		print ('Example==>"python test.py -i <filepath> -m <number_of_phrase> -n <number_of_words>"')
		sys.exit(0)
	try:
		txt_file = open(filename,'rb')
	except FileNotFoundError:
		print("Sorry, the file " + filename + " dose not exsit.")
		sys.exit(1)
	contents = txt_file.read()
	wordCount = word_operate(txt_file, contents, filename)
	wordCount.charsCount()
	wordCount.linesCount()
	wordCount.wordsCount()

if __name__ == "__main__":
	main(sys.argv[1:])
	