'''Lots of geeky customers visit our Amit's restaurant everyday. So, when asked to fill the feedback form, these customers represent the feedback using a binary string.
He has decided the following criteria to classify the feedback as Good or Bad :
If the string contains the substring "010" or "101", then the feedback is Good, else it is Bad.
So given some binary strings, you need to output whether according to the Amit, the strings are Good or Bad.

Input
The first line contains an integer T denoting the number of feedbacks. Each of the next T lines contains a string composed of only '0' and '1'.

Output
For every test case, print in a single line Good or Bad as per the Amit's method of classification.'''

T=int(input('Enter the number of testcases : '))
for i in range(T):
    string=input('Enter the binary string : ')
    x,y=string.find('010'),string.find('101')
    if x<0 and y<0:
        print('Bad')
    else:
        print('Good')