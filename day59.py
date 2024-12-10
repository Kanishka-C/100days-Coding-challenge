'''You are given the height H (in metres) and mass M (in kilograms) of Anusree. 
The Body Mass Index (BMI) of a person is computed as M/H^2.
Report the category into which Anusree falls, based on his BMI:
Category 1: Underweight if BMI ≤18
Category 2: Normal weight if BMI ∈{19, 20,…, 24}
Category 3: Overweight if BMI ∈{25, 26,…, 29}
Category 4: Obesity if BMI ≥30

Input:
The first line of input will contain an integer, T, which denotes the number of testcases. 
Then the testcases follow.
Each testcase contains a single line of input, with two space separated integers, M,H, which denote the mass and height of Anusree respectively.

Output:
For each testcase, output in a line, 1,2,3 or 4, based on the category in which Anusree falls.'''

T=int(input('Enter the number of testcases : '))
for i in range(T):
    M,H=map(int,(input('Enter mass and height : ').split()))
    bmi=M/(H*H)
    if bmi<=18:
        print('Category 1 (Underweight)')
    elif bmi<=24:
        print('Category 2 (Normal weight)')
    elif bmi<=29:
        print('Category 3 (Overweight)')
    else:
        print('Category 4 (Obesity)')