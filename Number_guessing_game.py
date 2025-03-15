import random 
a = int(input("Enter the starting number of range:"))
b = int(input("Enter the ending number of range:"))
num = random.randrange(a,b)
chances =7
print("You have 7 chances to guess the number.Guess correctly.")
while chances>=0:
    if chances == 0:
        print("You have Lost the game. Number is :",num)
        break
    
    ch = int(input("Guess the number : "))
    
    if ch == num:
        print("You have Guessed the number correct.")
        break 
    elif ch > num:
        print("Number Guessed is larger than the answer.")
    elif ch < num:
        print("Number Guessed is smaller than the answer.")
        
    chances -= 1
    print(f"You have {chances} chances")
    print()
    
print("Thank you for playing game.")