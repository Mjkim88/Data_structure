from collections import defaultdict, Counter
import numpy as np 
from scc import *
from dijsktra import *

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

# Construct word_user_dict(key=word, value=user)
def make_word_user_dic(data, num_line, space):
	dic = defaultdict(list)
	# append values
	for i in range(0, len(data), num_line):
		key = data[i+space].split('\n')[0]
		value = data[i].split('\n')[0]
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

def extract_num_value(dic):
	value_list = []
	for key in dic.keys():
		v = len(dic[key])
		value_list.append(v)
	return value_list

def extract_top5(key_list, index_list):
	top5_list = []
	for i in range(5):
		j = int(index_list[i])
		top5_list.append(key_list[j])
	return top5_list

def make_dfsvertex(dic):
	i=0
	vertices = []
	for key in dic.keys():
		key = DFSVertex()
		vertices.append(key)
		key.name = key
		key.n = i
		i+=1	
	return vertices

def make_print_scc(dic):
	vertices = []
	for key in dic.keys():
		vertex = DFSVertex(key)
		vertices.append(vertex)

	DFS = DepthFirstSearch()
	DFS.set_vertices(vertices)

	for vertex in vertices:
		friends = dic[vertex.name]
		for friend in friends:
			for node in vertices:
				if friend == node.name: 
					vertex.add(node)
	DFS.scc()

def shortest_path(dic, userID):
	g = Dijkstra()
	for key in dic.keys():
		user = g.add_vertex(key)
		if user.name == userID:
			user.d = 0
	for vertex in g.vertices:
		friends = dic[vertex.name]
		w = len(dic[vertex.name])
		for friend in friends:
			for node in g.vertices:
				if friend == node.name:
					vertex.add(node, w)
	g.shortest_path()
