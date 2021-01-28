from replit import clear 
import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10,10, 10, 10, 11]
user_cards = []
computer_cards = []

def first_deal():
  for i in cards:
   user_cards = sample(cards, 2)
   computer_cards = sample(cards, 2)
   user_hand_sum = sum(user_cards)
   comp_hand_sum = sum(computer_cards)
    
  end_of_game = False

  while not end_of_game:

    print(f"Your cards are now {user_cards} with a sum of {user_hand_sum}. The computers face card is {computer_cards[1]}.")

    if comp_hand_sum == 21:
      end_of_game = True
      print("The computer has a blackjack. You lose!")
      break
    elif user_hand_sum == 21:
      end_of_game = True
      print("You have a blackjack! You win!")
      break
    elif user_hand_sum > 21:
      if 11 in user_cards:
        if (user_hand_sum - 10 > 21):
          end_of_game = True
          print("You lose!")
          break
        else:
          new_user_hand_sum = user_hand_sum - 10

          print(f"Your ace has turned from 11 to 1. Your total sum is now {new_user_hand_sum}.")

          hit_or_pass = input("Do you want to hit or pass: ")

          if hit_or_pass == 'h':
            from random import choice
            random_card = (choice(cards))
            user_cards.append(random_card)
            user_hand_sum = sum(user_cards)
      else:
        end_of_game = True
        print(f"Your cards are over 21. You lose!")
        break
    else:  
      hit_or_pass = input("Do you want to hit or pass: ")
      if hit_or_pass == 'h':
        random_card = (choice(cards))
        user_cards.append(random_card)
        user_hand_sum = sum(user_cards)
      else:
        break
  print("It's the dealers turn. ")
  

  if comp_hand_sum < 18:
    random_card = (choice(cards))
    computer_cards.append(random_card)
    print(f"The dealer's cards are {computer_cards}. With a total of: {comp_hand_sum}. ")
  else:
    print(f"The dealers cards are {computer_cards}. With a total of {comp_hand_sum}.")

  if comp_hand_sum > user_hand_sum:
    print("You lose!")
  elif comp_hand_sum == user_hand_sum:
    print("Its a draw! ")
  elif comp_hand_sum < user_hand_sum:
    print("You win!")

play_game = input("Do you want to play a game of blackjack? Type 'y' for yes, 'n' for no: ")

if play_game == 'n':
  clear()
else:
  first_deal()
