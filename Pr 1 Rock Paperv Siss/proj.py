import random

# 0 = Rock, 1 = Paper, 2 = Scissors
yourchoice = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors: "))

if yourchoice < 0 or yourchoice > 2:
    print("Invalid choice! Please choose 0, 1, or 2.")
    exit()

compchoice = random.randint(0, 2)
choices = ["Rock", "Paper", "Scissors"]

print("You chose:", choices[yourchoice])
print("Computer chose:", choices[compchoice])

if yourchoice == compchoice:
    print("It's a tie!")
elif (yourchoice == 0 and compchoice == 2) or \
     (yourchoice == 1 and compchoice == 0) or \
     (yourchoice == 2 and compchoice == 1):
    print("You win!")
else:
    print("Computer wins!")
