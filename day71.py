'''There are N students in a class, where the i-th student has a score of Ai?.
The i-th student will boast if and only if the number of students scoring less than or equal Ai? is greater than the number of students scoring greater than Ai?.
Find the number of students who will boast.

Input Format
The first line contains T - the number of test cases. Then the test cases follow.
The first line of each test case contains a single integer N - the number of students.
The second line of each test case contains N integers 1,2,…,A1?,A2?,…,AN? - the scores of the students.

Output Format
For each test case, output in a single line the number of students who will boast.'''

T = int(input('Enter the number of test cases: '))
for _ in range(T):
    n=int(input('Enter the no of students : '))
    A=list(map(int,(input('Enter score of each student : ').split())))
    A.sort()
    students=0
    for i in range(n):
        less_or_equal=i+A.count(A[i])
        greater=n-less_or_equal
        if less_or_equal>greater:
            students+=1
    print(students)