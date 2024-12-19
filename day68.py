'''you will be given queries. Each query is of one of the following three types: :

Add an element to the set. : 1
Delete an element from the set. (If the number is not present in the set, then do nothing). : 2
If the number is present in the set, then print "Yes" else print "No". : 3

Input Format
The first line of the input contains the number of queries. The next lines contain query each. Each query consists of two integers the type of the query and an integer.

Output Format
Print "Yes" if the number is present in the set and if the number is not present, then print "No".'''

n = int(input('Enter the number of queries : '))
arr=[]
for _ in range(n):
    query_type,element=map(int,(input('Enter type and the element : ').split()))
    element=str(element)
    if query_type==1:
        arr.append(element)
    elif query_type==2:
        if element in arr :
            arr.remove(element)
    elif query_type==3:
        val =''.join(arr)
        if val.find(element)!=-1:
            print('Yes')
        else:
            print('No')