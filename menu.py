from functions import *

#read txt file
u = readtxt('user.txt')
f = readtxt('friend.txt')
w = readtxt('word.txt')

def read_data_file():
	# count number of users
	user = int(round(len(u)/4) + 1)
	friendship = int(round(len(f)/3) + 1)
	tweets = int(round(len(w)/4) + 1)

	# print the results
	print "Total users: %d" %user
	print "Total friendship records: %d" %friendship
	print "Total tweets: %d" %tweets

def display_statistics():
	# Construct Hashtable(Dictionary)(key=user, value=friend, word for each)
	user_friendship = make_dic(f, 3, 1)
	tweet_list = make_dic(w, 4, 2)

	# Count the number of the values
	friend_avg, friend_min, friend_max = stat(user_friendship)
	tweets_avg, tweets_min, tweets_max = stat(tweet_list)

	print 'Average number of friends: %f' % friend_avg
	print 'Minimum friends: %d' % friend_min
	print 'Maximum number of friends: %d' % friend_max 
	print ' '
	print 'Average tweets per user: %f' % tweets_avg
	print 'Minimum tweets per user: %d' % tweets_min
	print 'Maximum tweets per user: %d' % tweets_max 

def top5_words():
	# Construct word_dict(key=word, value=count)
	word_dict = make_count_dic(w, 4, 2)
	# Extract the values
	word_count_list = extract_value(word_dict)
	# Heap sort the list
	word_count_list = heapsort(word_count_list)
	# Find the top 5 words
	top5_word = extract_top5(word_dict, word_count_list)
	print top5_word

def top5_users():
	return 0

def find_users():
	# Construct word_user_dict(key=word, value=user)
	word_user_dic = make_word_user_dic(w, 4, 2)
 	# Get the word to be searched
	word = raw_input("type the word tweeted:")
	# Find the users who tweeted word
	user_list = word_user_dic[word]
	print user_list

def find_friend_user():
	# Construct word_user_dict(key=word, value=user)
	word_user_dic = make_word_user_dic(w, 4, 2)
	# Get the word to be searched
	word = raw_input("type the word tweeted:")
	# Get the list of users who tweeted word
	user_list = word_user_dic[word]

	# Construct friendship_dict(key=user, value=friend)
	user_friendship = make_dic(f, 3, 1)
	# Make the list of users' friend
	friend_list = []
	for i in range(len(user_list)):
		friends = []
		friends = user_friendship.get(user_list[i])
		friend_list += friends
	print friend_list

def delete_meantions():
	return 0

def delete_user():
	# Make user list
	all_users = make_user_list(u, 4)
	# Construct word_user_dict(key=word, value=user)
	word_user_dic = make_word_user_dic(w, 4, 2)
	# Get the word to be searched
	word = raw_input("type the tweeted word:")
	# Get the list of users who tweeted word
	user_list = word_user_dic[word]	

	# Delete users
	for i in range(len(user_list)):
		all_users.remove(user_list[i])

	print all_users	



# def fine_scs():