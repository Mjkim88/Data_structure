from collections import defaultdict
import numpy as np
from heap import *


def readtxt(file):
	f = open(file,'r')
	f.close
	f = f.readlines()
	return f

def make_count_dic(data, num_line, space):
	dic = defaultdict(list)
	# append values
	for i in range(0, len(data), num_line):
		key = data[i+space].split('\n')[0]
		dic[key] = 0
	for i in range(0, len(data), num_line):
		key = data[i+space].split('\n')[0]
		dic[key] += 1
	return dic

def extract_value(dic):
	value_list = []
	for key in dic:
		value_list.append(dic[key])
	return value_list

def extract_top5(dic, count_list):
	top5_list = []
	for i in range(5):
		top5_list.append(dic.keys()[dic.values().index(count_list[i])])
	return top5_list

# Read txt file
u = readtxt('user.txt')
f = readtxt('friend.txt')
w = readtxt('word.txt')

# Construct Hashtable(Dictionary) for counting tweeted words
word_dict = make_count_dic(w, 4, 2)

# Extract the values
word_count_list = extract_value(word_dict)

# Heap sort the list
word_count_list = heapsort(word_count_list)

# Find the top 5 words
top5_word = extract_top5(word_dict, word_count_list)

print top5_word
