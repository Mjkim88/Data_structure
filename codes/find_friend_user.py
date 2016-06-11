from collections import defaultdict
import numpy as np 

def readtxt(file):
	f = open(file,'r')
	f.close
	f = f.readlines()
	return f

# Read txt file
u = readtxt('user.txt')
f = readtxt('friend.txt')
w = readtxt('word.txt')

def make_word_user_dic(data, num_line, space):
	dic = defaultdict(list)
	# append values
	for i in range(0, len(data), num_line):
		key = data[i+space].split('\n')[0]
		value = data[i].split('\n')[0]
		dic[key].append(value)
	return dic

word_user_dic = make_word_user_dic(w, 4, 2)
word = raw_input("type the word tweeted:")
user_list = word_user_dic[word]

def make_dic(data, num_line, space):
	dic = defaultdict(list)
	# append values
	for i in range(0, len(data), num_line):
		key = data[i].split('\n')[0]
		value = data[i+space].split('\n')[0]
		dic[key].append(value)
	return dic

user_friendship = make_dic(f, 3, 1)

friend_list = []
for i in range(len(user_list)):
	friends = []
	friends = user_friendship.get(user_list[i])
	friend_list += friends

print friend_list