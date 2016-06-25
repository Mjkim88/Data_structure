from functions import *
from menu import *

# Make data structure: Hashtable
# read txt file
u = readtxt('user.txt')
f = readtxt('friend.txt')
w = readtxt('word.txt')

# Construct Hashtable(Dictionary)(key=user, value=friend) 
user_friendship = make_dic(f, 3, 1)
# Construct Hashtable(Dictionary)(key=user, value=word)
tweet_dic= make_dic(w, 4, 2)
# Construct word_user_dict(key=word, value=user)
word_user_dic = make_word_user_dic(w, 4, 2)

print "0. Read data files"
print "1. display statistics"
print "2. Top 5 most tweeted words"
print "3. Top 5 most tweeted users"
print "4. Find users who tweeted a word"
print "5. Find all people who are friends of the above users"
print "6. Delete all mentions of a word"
print "7. Delete all users who mentioned a word"
print "8. Find strongly connected components"
print "9. Find shortest path from a given user"
print "99. Quit"

Menu = raw_input("Select Menu: ")

while Menu != '99':
	if Menu == '0':
		read_data_file(user_friendship, tweet_dic)

	elif Menu == '1':
		display_statistics(user_friendship, tweet_dic)

	elif Menu == '2':
		top5(word_user_dic)

	elif Menu == '3':
		top5(tweet_dic)

	elif Menu == '4':
		find_users(word_user_dic)

	elif Menu == '5':
		find_friend_user(word_user_dic, user_friendship)

	elif Menu == '6':
		tweet_dic, word_user_dic = delete_meantions(tweet_dic, word_user_dic)

	elif Menu == '7':
		user_friendship, tweet_dic, word_user_dic = delete_user(user_friendship, tweet_dic, word_user_dic)

	elif Menu == '8':
		find_scc(user_friendship)

	elif Menu == '9':
		find_shortest_path(user_friendship)
		
	else: 
		print "Not available number"
	print " "	
	Menu = raw_input("Select Menu: ")