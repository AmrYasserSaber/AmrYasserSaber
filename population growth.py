from typing import Counter


S=int(input("input the starting number"))

E=int(input("input the end number"))

Counter = 0

while E < 0 or S < 0:
    if E < 0:
        E=int(input("input a positive number") )
    else:
        S=int ( input("input a positive number") )
    
while S < 9:
    S=int ( input("the starting number should be more than 9 \n") );    

while E < S:
    E=int ( input("input an end number biger than the starting one") );

while S < E :
    S= S + int(S/3) - int(S/4)
    Counter = Counter+1

print("the number of years it takes is : "+ str(Counter))

