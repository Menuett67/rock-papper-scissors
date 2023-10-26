from replit import clear
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game=[rock,paper,scissors]
should_continue=True
while should_continue:
 user_choice=int(input("what do you choose?Type 0 for rock,1 for paper and 2 for scissors:"))
 print(game[user_choice])
 computer_choice=random.randint(0,2)
 print(game[computer_choice])
 if computer_choice==user_choice:
  print("it's a draw.")
 elif computer_choice==2 and user_choice==0:
  print("you won.")
 elif user_choice==2 and computer_choice==0:
  print("you lose")
 elif computer_choice<user_choice:
  print("you won.")
 elif user_choice<computer_choice:
  print("you lose.")
 ask_to_continue=input("do you want to continue the game?type 'yes' to continue, or Type 'no' to exit:") 
 if ask_to_continue=="yes":
  clear()
 elif ask_to_continue=="no":
   print("you did not want to continue the game and the game finished.")
   should_continue=False
