from collections import defaultdict
import numpy as np 
reload(sys)

def readtxt(file):
	f = open(file,'r')
	f.close
	f = f.readlines()
	return f

# Construct Hashtable(Dictionary)(key=user, value=friend or word)
def make_dic(data, num_line, space):
	dic = defaultdict(list)
	# append values
	for i in range(0, len(data), num_line):
		key = data[i].split('\n')[0]
		value = data[i+space].split('\n')[0]
		dic[key].append(value)
	return dic

def make_user_list(data, num_line):
	all_users = []
	for i in range(0, len(data), num_line):
		user = data[i].split('\n')[0]
		all_users.append(user)
	return all_users

def stat(dic):
	num_list = []
	for key in dic:
		size = len(dic[key])
		num_list.append(size)
	avg = np.mean(num_list)
	minimum = min(num_list)
	maximum = max(num_list)
	return avg, minimum, maximum

# Construct word_dict(key=word, value=count)
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
		# key = key.encode('utf-8')
		value_list.append(dic[key])
	return value_list

def extract_top5(dic, count_list):
	top5_list = []
	for i in range(500):
		top5_list.append(dic.keys()[dic.values().index(count_list[i])])
	return top5_list

# Construct word_user_dict(key=word, value=user)
def make_word_user_dic(data, num_line, space):
	dic = defaultdict(list)
	# append values
	for i in range(0, len(data), num_line):
		key = data[i+space].split('\n')[0]
		value = data[i].split('\n')[0]
		dic[key].append(value)
	return dic

# heapsort
def parent(n):
	return (n-1)/2

def left(n):
	return 2*n+1

def right(n):
	return 2*n+2

def heapify(A, i, heapsize):
	l = left(i) 
	r = right(i)
	if l < heapsize and A[l] < A[i]:
		largest = l
	else:
		largest = i
	if r < heapsize and A[r] < A[largest]:
		largest = r
	if largest !=i:
		A[i], A[largest] = A[largest], A[i]
		heapify(A, largest, heapsize)
	return A

def buildheap(A):
	for i in range(len(A)/2+1, 0, -1):
		heapify(A, i-1, len(A))

def heapsort(A):
	buildheap(A)
	for i in range(len(A), 1, -1):
		A[i-1],A[0] = A[0],A[i-1]
		heapify(A,0,i-1)
	return A