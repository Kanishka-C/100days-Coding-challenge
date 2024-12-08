'''Anusree is struggling to pass a certain college course.
The test has a total of N question, each question carries 3 marks for a correct answer and −1 for an incorrect answer. Anusree is a risk-averse person so he decided to attempt all the questions. 
It is known that Anusree got X questions correct and the rest of them incorrect. For Anusree to pass the course he must score at least P marks.
Will Anusree be able to pass the exam or not?
Input Format
First line will contain T, number of testcases. Then the testcases follow.
Each testcase contains of a single line of input, three integers N, X, P.
Output Format
For each test case output ""PASS"" if Chef passes the exam and ""FAIL"" if Chef fails the exam.'''
T=int(input('Enter the number of testcases : '))
for i in range (T):
    N,X,P=map(int,(input('Enter the values of N,X,P : ').split()))
    marks=(X*3)+((N-X)*-1)  #3 marks for each correct ans and -1 for each wrong ans
    if marks < P:
        print('Fail')
    else:
        print('Pass')