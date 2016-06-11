from collections import defaultdict
import numpy as np 

def readtxt(file):
	f = open(file,'r')
	f.close
	f = f.readlines()
	return f

u = readtxt('user.txt')
f = readtxt('friend.txt')
w = readtxt('word.txt')

def make_user_list(data, num_line,):
	all_users = []
	for i in range(0, len(data), num_line):
		user = data[i].split('\n')[0]
		all_users.append(user)
	return all_users

def make_word_user_dic(data, num_line, space):
	dic = defaultdict(list)
	# append values
	for i in range(0, len(data), num_line):
		key = data[i+space].split('\n')[0]
		value = data[i].split('\n')[0]
		dic[key].append(value)
	return dic

all_users = make_user_list(u, 4)
print all_users
word_user_dic = make_word_user_dic(w, 4, 2)
word = raw_input("type the word tweeted:")
user_list = word_user_dic[word]
print user_list

for i in range(len(user_list)):
	all_users.remove(user_list[i])

print all_users