from functions import *
from scc import *
import numpy as np 

def read_data_file(user_friendship, tweet_dic):
	# count number of users
	user = len(user_friendship)
	friendship = sum(len(v) for v in user_friendship.itervalues())
	tweets = sum(len(v) for v in tweet_dic.itervalues())

	# print the results
	print "Total users: %d" %user
	print "Total friendship records: %d" %friendship
	print "Total tweets: %d" %tweets

def display_statistics(user_friendship, tweet_dic):
	# Count the number of the values
	friend_avg, friend_min, friend_max = stat(user_friendship)
	tweets_avg, tweets_min, tweets_max = stat(tweet_dic)

	print 'Average number of friends: %f' % friend_avg
	print 'Minimum friends: %d' % friend_min
	print 'Maximum number of friends: %d' % friend_max 
	print ' '
	print 'Average tweets per user: %f' % tweets_avg
	print 'Minimum tweets per user: %d' % tweets_min
	print 'Maximum tweets per user: %d' % tweets_max 

def top5(dic):
	key_list = []
	for key in dic.keys():
		key_list.append(key)
	# Extract the number of values and sort and get the indices 
	count_list = extract_num_value(dic)
	index_list = range(len(count_list))
	index_list.sort(key=lambda n:count_list[n])
	index_list.reverse()
	# Find the top 5 words
	top5 = extract_top5(key_list, index_list)
	print top5

def find_users(dic):
 	# Get the word to be searched
	word = raw_input("type the word tweeted:")
	# Find the users who tweeted word
	user_list = dic[word]
	print user_list

def find_friend_user(word_user_dic, user_friendship):
	# Get the word to be searched
	word = raw_input("type the word tweeted:")
	# Get the list of users who tweeted word
	user_list = word_user_dic[word]
	# Make the list of users' friend
	friend_list = []
	for i in range(len(user_list)):
		friends = []
		friends = user_friendship.get(user_list[i])
		friend_list += friends
	print friend_list

def delete_meantions(tweet_dic, word_user_dic):
	# Get the word to be searched
	word = raw_input("type the word tweeted:")	
	# Delete the word from tweet_dic
	user_list = word_user_dic[word]	
	for user in user_list:
		try:
			tweet_dic[user].remove(word)
		except ValueError:
			pass	
	# Delete the word from word_user_dic	
	try:
		del word_user_dic[word]
	except KeyError:
		pass
	return tweet_dic, word_user_dic

def delete_user(user_friendship, tweet_dic, word_user_dic):
	# Get the word to be searched
	word = raw_input("type the tweeted word:")
	user_list = word_user_dic[word]
	for user in user_list:
		try:
			del user_friendship[user]
			del tweet_dic[user]
		except KeyError:
			pass
		try:	
			word_user_dic[word].remove(user)
		except ValueError:
			pass
	return user_friendship, tweet_dic, word_user_dic

def find_scc(user_friendship):
	make_print_scc(user_friendship)
	return 0

def shortest_path():
	return 0