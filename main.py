import random
from art import logo
def draw_card(cards,deck,score):
  card=random.choice(cards)
  if(card==11 and score[0]>=11):
    card=1
  deck.append(card)
  score[0]+=card
  return card

def game(cards,user_cards,comp_cards,user_score,comp_score,flag):
  for i in range (0,2):
    draw_card(cards,user_cards,user_score)
    draw_card(cards,comp_cards,comp_score)
  print(f"your cards are : {user_cards}, your score : {user_score}")
  print(f"Comp card is {comp_cards[0]}")
  choice=input("Type 'y' to get another card, type 'n' to pass: ")
  while choice=="y" or user_score[0]<17:
    if(user_score[0]<17):
      print("You Score is below 17, automatically a card is chosen for you")
    draw_card(cards,user_cards,user_score)
    if(user_score[0]>21):
      flag[0]=2
      return
    print(f"your cards are : {user_cards}, your score : {user_score[0]}")
    choice=input("Type 'y' to get another card, type 'n' to pass: ")
  while(comp_score[0]<17):
    draw_card(cards,comp_cards,comp_score)
    if(comp_score[0]>21):
      flag[0]=1
      return

def play():
  print(logo)
  cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
  user_cards=[]
  comp_cards=[]
  user_score=[0]
  comp_score=[0]
  flag=[0]
  game(cards,user_cards,comp_cards,user_score,comp_score,flag)
  if(flag[0]==0):
    if(user_score>comp_score):
      print("User Won")
      print(f"User Score : {user_score[0]}, Computer Score : {comp_score[0]}")
    elif (user_score==comp_score):
      print("Draw")
    else:
      print("Computer Won")
      print(f"User Score : {user_score[0]}, Computer Score : {comp_score[0]}")
  elif (flag[0]==1):
    print("Computer Score exceed the limit")
    print("User Won")
  else:
    print("Your Score exceed the limit")
    print("Computer Won")



choice=input("Do you want to play(y/n) : ")
while(choice=="y"):
  play()
  choice=input("Want to play again(y/n) : ")
print("GoodBye")  
  

