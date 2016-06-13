from functions import *
from menu import *

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

if Menu == '0':
	read_data_file()

elif Menu == '1':
	display_statistics()

elif Menu == '2':
	top5_words()

elif Menu == '3':
	top5_users()

elif Menu == '4':
	find_users()

elif Menu == '5':
	find_friend_user()

elif Menu == '6':
	delete_meantions()

elif Menu == '7':
	delete_user()

elif Menu == '8':
	fine_scs()
	