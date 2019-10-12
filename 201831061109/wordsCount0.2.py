# coding=utf-8
import re
import sys
import getopt

from sys import argv
script, filename = argv

global number = 0

class word_operate():
    def __init__(self, txt_file, contents, c_filename):
        self.txt_file = txt_file
        self.contents = contents
        self.c_filename = c_filename

    def charsCount(self):
        chars = contents.rstrip()
        num_words = len(chars)
        print(f'characters:{num_words}')

    def linesCount(self):
        file = open(filename)
        list = file.readlines()  # 将文件读取到列表中，每行一元素
        count = 0
        for line in list:
            count += 1
        print(f'Lines:{count}')

    def wordsCount(self):
        contents = self.contents.decode('utf-8')
        words_arr = re.findall(r'\w{4,}', contents.lower())  # 匹配字符数大于4的单词
        words_num = len(words_arr)
        print(f'words:{words_num}')

        count_num = {}
        for word in words_arr:
            count_num[word] = count_num.get(word, 0) + 1  # 利用字典的get方法，将单词作为键，单词出现频率为值；若单词首次出现，默认键值为0

        counts_list = list(count_num.items())  # 将字典转化为列表，方便后续输出
        counts_list.sort(key=lambda x: x[1], reverse=True)  # 对列表中每个元素的第二个字段排序，及单词出现频率

        for i in range(number):
            word, count = counts_list[i]
            print(f'{word}:{count}')


def findword(n):#传入指定长度参数n
    words_arr = re.findall(r'\w{4,}', contents.lower())  # 匹配字符数大于4的单词
    wordDict = {}
    for word in words_arr:
        wordDict[word] = wordDict.get(word, 0) + 1  # 利用字典的get方法，将单词作为键，方便查询避免单词重复出现
    for key in wordDict
        if len(key) == n:     #计算键长与目标长度匹配
            print (f'{key}\n')


def main(argv):
    #filename = ''
    try:
        opts, args = getopt.getopt(argv, "i:mn", ["path=", "phrase=","numbers"])
    except getopt.GetoptError:
        print 'test.py -i <filepath> -m <number_of_phrase> -n <number_of_words>'
    for opt,arg in opts:
        if opt == '-i':
            filename = arg
        elif opt == '-n':
            number = arg



if __name__ == "__main__":
    main(sys.argv[1:])
    if filename == '':
        print("Please enter the '-i' parameter!")
        sys.exit(0)
    else:
        txt_file = open(filename,'rb')
        contents = txt_file.read()
        wordCount = word_operate(txt_file, contents)
        wordCount.charsCount()
        wordCount.linesCount()
        wordCount.wordsCount()