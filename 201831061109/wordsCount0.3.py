# coding=utf-8
import re
import sys
import getopt

number = 10
isSave = False
outfile = ''

class word_operate():
	def __init__(self, txt_file, contents, c_filename):
		self.txt_file = txt_file
		self.contents = contents
		self.c_filename = c_filename

	def charsCount(self):
		chars = self.contents.rstrip()
		num_words = len(chars)
		if isSave == False:
			print(f'characters:{num_words}')
		else:
			print("The results will be saved in " + outfile )
			print(f'characters:{num_words}')
			try:
				doc = open(f'{outfile}','a')
				print(f'characters:{num_words}',file = doc)
			except FileNotFoundError:
				print("Sorry, the file " + outfile + " dose not exsit.")
				sys.exit(1)

	def linesCount(self):
		file = open(self.c_filename)
		list = file.readlines()  # 将文件读取到列表中，每行一元素
		count = 0
		for line in list:
			count += 1
		if isSave == False:
			print(f'Lines:{count}')
		else:
			print(f'Lines:{count}')
			doc = open(f'{outfile}','a')
			print(f'Lines:{count}',file = doc)

	def wordsCount(self):
		contents = self.contents.decode('utf-8')
		words_arr = re.findall(r'\w{4,}', contents.lower())  # 匹配字符数大于4的单词
		words_num = len(words_arr)
		if isSave == False:
			print(f'words:{words_num}')
		else:
			print(f'words:{words_num}')
			doc = open(f'{outfile}','a')
			print(f'words:{words_num}', file = doc)

		count_num = {}
		for word in words_arr:
			count_num[word] = count_num.get(word, 0) + 1  # 利用字典的get方法，将单词作为键，单词出现频率为值；若单词首次出现，默认键值为0

		counts_list = list(count_num.items())  # 将字典转化为列表，方便后续输出
		counts_list.sort(key=lambda x: x[1], reverse=True)  # 对列表中每个元素的第二个字段排序，及单词出现频率

		for i in range(number):
			word, count = counts_list[i]
			if isSave == False: 
				print(f'{word}:{count}')
			else:
				print(f'{word}:{count}')
				doc = open(f'{outfile}', 'a')
				print(f'{word}:{count}', file = doc)



def main(argv):
	global number
	global isSave, outfile
	filename = ""
	contents = ""
	try:
		opts, args = getopt.getopt(argv, "m:n:i:o:")
	except getopt.GetoptError:
		print ('test.py -i <filepath> -m <number_of_phrase> -n <number_of_words> -o <outfile_path>')
	for opt,arg in opts:
		if opt == '-i':
			filename = arg
		elif opt == '-n':
			if arg.isdigit():
				number = int(arg)
			elif (arg.isdigit() and int(arg) > 10):
				print("-n para is lower than 10!")
				sys.exit(1)
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
	