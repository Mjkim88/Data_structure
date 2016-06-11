def readtxt(file):
	f = open(file,'r')
	f.close
	f = f.readlines()
	return f

#read txt file
u = readtxt('user.txt')
f = readtxt('friend.txt')
w = readtxt('word.txt')

# count number of users
user = int(round(len(u)/4) + 1)
friendship = int(round(len(f)/3) + 1)
tweets = int(round(len(w)/4) + 1)

# print the results
print "Total users: %d" %user
print "Total friendship records: %d" %friendship
print "Total tweets: %d" %tweets