import random 

print("ROCK PAPER SCISSOR ")
print("Rules:-")
print("You have to win atleast 3 times to win the match.")

d1 = {1:"Rock",2:"Paper",3:"Scissor"}
user_winnings,computer_winnings = 1,1
cnt = 0

while user_winnings < 3 and  computer_winnings < 3:
    
    #user and computer selection
    print("select one of the following number :")
    for num,val in d1.items():
        print(f"{num} : {val}")
    try:
        user_ch = int(input())
    except AttributeError :
        print("The number must be an integer.Please enter again.")
        continue 
   
    if user_ch < 1 or user_ch > 3:
        print("The input provided should be in the range of 1 to 3. Please enter again.")
        continue
    
    computer_ch = random.randrange(1,4)
    print("Computer chose : ",d1[computer_ch])
    print()
    
    #comparisions
    '''
    Winning Rules:
    Rock vs paper-> paper wins
    Rock vs scissor-> Rock wins
    paper vs scissor-> scissor wins
    '''
    if user_ch == computer_ch:
        print("Draw.\nBoth get one point each.")
        user_winnings += 1
        computer_winnings += 1
    else:
        if user_ch == 1:
            if computer_ch == 2:
                print(" + 1 point to Computer")
                computer_winnings += 1
            elif computer_ch == 3:
                print(" + 1 point to User.")
                user_ch += 1
        elif user_ch == 2:
            if computer_ch == 1:
                print(" + 1 point to User.")
                user_winnings += 1 
            elif computer_ch == 3:
                print(" + 1 point to Computer")
                computer_ch += 1
        elif user_ch == 3:
            if computer_ch == 1:
                print(" + 1 point to Computer")
                computer_ch += 1
            elif computer_ch == 2:
                print(" + 1 point to User")
                user_ch += 1
        
    print(f"After round {cnt + 1}, the scores are as follows:\nUser : {user_winnings}\nComputer : {computer_winnings}")
    print()
    cnt += 1
    
if user_winnings == 3 and computer_winnings == 3:
    print("Its a Draw !!!")
elif user_winnings == 3:
    print("User won the match!!!!")
else:
    print("Computer won the match!!!")

print("Thank You for playing.")        