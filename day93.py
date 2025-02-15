'''Ilya found a social network called "TheScorpyBook.com". It currently has N registered users. As in any social network two users can be friends. 
Ilya wants the world to be as connected as possible, so he wants to suggest friendship to some pairs of users. He will suggest user u to have a friendship with user v if they are not friends yet and there is a user w who is friends of both of them. 
Note that u, v and w are different users. Ilya is too busy with IPO these days, so he asks you to count how many friendship suggestions he has to send over his social network.

Input
The first line contains an integer number N — the number of users in the network. 
Next N lines contain N characters each denoting friendship relations. jth character if the ith lines equals one, if users i and j are friends and equals to zero otherwise. This relation is symmetric, i.e. if user a is friend of b then b is also a friend of a.

Output
A single integer — number of friendship suggestions Ilya has to send.'''
n=int(input('Enter no of users : '))
print('Enter the friends matrix : ')
friends = [list(map(int, input().strip())) for _ in range(n)]
#print(friends)
req=0
for i in range(n):
    for j in range(n):
         if i!=j and friends[i][j]==1:
            for k in range(n):
              if i != k and j != k and friends[i][k] == 1 and friends[j][k] == 0:
                    #sugg.add((min(j, k), max(j, k)))   Ensure unique pairs
                    req+=1
print(req)