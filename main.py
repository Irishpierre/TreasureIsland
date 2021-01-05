#Treasure Island Game 

#Intro
print("Welcome to Treasure Island!")
print("Your goal is to find the treasure.")

#Ask the first question
choice1 = input("You're at a crossroad, where do you want to go? (Type 'Left' or 'Right') \n").lower()


#Control flow for user choices
#Choice1 Game over 
if choice1 == "right":
  print("You fell into a spike trap! Game Over.")
#Continue the story
if choice1 == "left":
  choice2 = input("You've avoided a spike trap and continue down the path! There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. \n").lower()
  #Choice2 decisions. Continue the nested control flow
  #This is the correct answer, continue the nest 
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed! There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose? \n").lower()
    #Choice3 options. Two losing, 1 win 
    if choice3 == "red":
      print("It's a room filled with fire! Game Over.") #Lose
    elif choice3 == "yellow":
      print("You found the treasure! You win!") #Win
    elif choice3 == "blue":
      print("There's a tiger behind this door! He eats you! Game over.") #Lose
    else:
      print("That's not a door!") #Choice3 Invalid
  
  #Choice2 fail
  else:
    print("You were eaten by the largest Trout the world has ever seen.")

#Invalid option from choice1 
else:
  print("Invalid option")

