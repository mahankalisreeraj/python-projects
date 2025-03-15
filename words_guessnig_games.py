import random 

words = [ "apple", "zebra", "mountain", "ocean", "guitar", "python", "galaxy", "sunshine", "whisper", "volcano",
    "mystery", "jungle", "rocket", "horizon", "adventure", "puzzle", "dragon", "tornado", "umbrella", "fireworks",
    "comet", "echo", "shadow", "butterfly", "canyon", "island", "treasure", "lantern", "midnight", "thunder",
    "phantom", "mirror", "waterfall", "crystal", "storm", "meadow", "spectrum", "labyrinth", "paradise", "twilight",
    "stardust", "nebula", "harmony", "voyage", "compass", "infinity", "cascade", "radiance", "whirlpool", "serenity",
    "breeze", "illusion", "glacier", "horizon", "eclipse", "flame", "zenith", "melody", "mirage", "pulse"]

rand_word = random.choice(words)
n = len(rand_word)
hints = [f"The first letter of the word is {rand_word[0]}",f"The last letter of the word is {rand_word[n-1]}"]

hints_cnt = 2
chances = 12

ans = ["_"]*len(rand_word)

print("Welcome to word Guessing game.")
print("Rules :-")
print("1) You have 2 hints.Use them wisely")
print("2) You have 12 chances")
print()

while chances > 0 :
    ch = input("Guess the word : ").lower()
    
    if ch.isalpha() and len(ch) != 1:
        print("Enter only single character!!")
        continue 
    
    if ch in rand_word:
        print("It's a correct guess")
        for i in range(n):
            if rand_word[i] == ch:
                ans[i] = ch 
    else:
        print("Wrong guess.")
        chances -= 1
        print(f"You have {chances} chances")
        
    print()
    if hints_cnt > 0:
        choice = input(" Do you want a hint? (y/n): ").lower()
        if choice == 'y':
            hint_to_give = hints.pop(0)  
            print(f"Hint: {hint_to_give}")
            hints_cnt -= 1

            if hint_to_give.startswith("The first letter"):
                ans[0] = rand_word[0]
            else:
                ans[-1] = rand_word[-1]
        
    print()
    print(ans)
    if ans.count("_") == 0:
        print("You have won the game.🎉🎉")
        break 
    
if chances == 0:
    print("You lost the game.Word is ",rand_word)
print("Thank you for playing the game.")