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

def make_dic(data, num_line, space):
	dic = defaultdict(list)
	# append values
	for i in range(0, len(data), num_line):
		key = data[i].split('\n')[0]
		value = data[i+space].split('\n')[0]
		dic[key].append(value)
	return dic

def count_value(dic):
	num_list = []
	for key in dic:
		size = len(dic[key])
		num_list.append(size)
	avg = np.mean(num_list)
	minimum = min(num_list)
	maximum = max(num_list)
	return avg, minimum, maximum

# Construct Hashtable(Dictionary)
user_friendship = make_dic(f, 3, 1)
tweet_list = make_dic(w, 4, 2)

# Count the number of the values
friend_avg, friend_min, friend_max = count_value(user_friendship)
tweets_avg, tweets_min, tweets_max = count_value(tweet_list)


print 'Average number of friends: %f' % friend_avg
print 'Minimum friends: %d' % friend_min
print 'Maximum number of friends: %d' % friend_max 
print ' '
print 'Average tweets per user: %f' % tweets_avg
print 'Minimum tweets per user: %d' % tweets_min
print 'Maximum tweets per user: %d' % tweets_max 


# Construct key of Hashtable(Dictionary)
# user_friendship = defaultdict(list)
# # for i in range(0, len(u), 4):
# # 	user_id = u[i].split('\n')[0]
# # 	user_friendship[user_id] = {}

# # Construct value of Hashtable
# for i in range(0, len(f), 3):
# 	user_id = f[i].split('\n')[0]
# 	friend_id = f[i+1].split('\n')[0]
# 	user_friendship[user_id].append(friend_id)