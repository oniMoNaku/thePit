# today is 389e
# the python pit
# magPi - 01

# PUTTING TEXT ONTO THE SCREEN
print("*** Welcome to The Python Pit! ***")
print() # A line space
print("Brought to you by The MagPi")
print()

# ARITHMETIC
print("Arithmetic")
print("Two plus two equals ",2+2); print()
print("Eight minus three equals ",8-3); print()
print("Four times two equals ",4*2); print()
print("Ten divided by two equals ",10/2); print()

# SPARE ME THE DETAILS
print("Division")
print("Seven divided by three is",7/3); print()
print("Seven divided by three is roughly",int(7/3)); print()
print("Five divided by two is",5/2); print()
print("Five divided by two is roughly",int(5/2)); print()

# ALGEBRA
print("Algebra")
a = 3
b = 7
c = 4
print("A is equal to",a); print()
print("B is equal to",b); print()
print("C is equal to",c); print()
print("A plus B equals",a+b); print()
print("A plus B plus C equals",a+b+c); print()
print("A plus B minus C equals",a+b-c); print()

# STRINGS OF WORDS
print("Strings")
a = "If you"
b = "notice"
c = "this"
d = "you will"
e = "is not worth"
f = "noticing!"
print(a,b,c,b,d,b,c,b,e,f); print()

# COUNTING WITH FOR LOOPS
print("For Loops")
for n in range(0,10+1):
    print(n)
print()
for n in range(100,0-1,-10):
    print(n)
print()

# COUNTING WITH WHILE LOOPS
print("While Loops")
n=0
while n <= 10:
    print (n)
    n += 1
print()
print("While backwards")
n=10
while n >= 0:
    print (n)
    n -= 1
print()

# LOTTERY NUMBERS
import random
print("Random Numbers")
for n in range(1,6+1): # We want six random numbers
    print (random.randint(1,100)) # Picks a number between 1 and 100
print()

# BINGO!
import random
print("Bingo")
n =0; count =0
while n != 13: # Keep looping till you get thirteen
    n = random.randint(1,100); count += 1
print (count); print()

# STRING ARRAYS
mytext = ["I", "Love", "My","Raspberry","Pi"]
for n in range(0,5):
    print (mytext[n])
print()


    
