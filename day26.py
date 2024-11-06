#Maximum number of handshakes
import math
n=int(input('Enter the number of people in the room : '))
no_of_handshakes=(math.factorial(n))/(math.factorial(2)*(math.factorial(n-2)))
print(int(no_of_handshakes))