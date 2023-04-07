friends=input("enter three friends names, sparated by commas (no spaces,Please!").split(',')

peopleFile=open('people.txt','r')
people=[line.strip() for line in  peopleFile.readlines()]
peopleFile.close()

nearFriendsFile=open('nearPeople.txt','w')


peopleSet=set(people)
friendsSet=set(friends)
nearByFriends=peopleSet.intersection(friendsSet)
for nearByFriend in nearByFriends:
    nearFriendsFile.write(f'{nearByFriend}\n')
nearFriendsFile.close()