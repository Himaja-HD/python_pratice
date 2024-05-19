"""
#List
student_name = ['Raju',10, 20.25, 'M']
print(student_name)

"""

import random

user_choice = input("Enter your choice- Rock, Paper, Scissor = ")
computer_choice = random.choice(['Rock', 'Paper', 'Scissor'])

print(user_choice, computer_choice)

if user_choice == computer_choice:
    print('Match has been Tied!')

elif user_choice == 'Rock':
    if computer_choice == 'Paper':
        print("Paper covers rock! Compyter wins!")
    else:
        print("Rock smashes scissor! You win!")

elif user_choice == 'Paper':
    if computer_choice == 'Rock':
        print("Paper covers rock! You win")
    else:
        print("Scissor cuts paper! computer won")

elif user_choice == 'Scissor':
    if computer_choice == 'Rock':
        print('Rock smashes scissor! computer won')
    else:
        print('Scissor cuts paper! You won')

else:
    print("Wrong input! Re-enter")
