print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice_1=input('you are at a crossroad ,where do you want to go?Type "left" or "right"\n ').lower()
if choice_1 == "left":
    choice_2=input('you\'ve come to a lake , there is an island in middle of a lake type'
                    ' wait to wait for boat or type swim to swim across the lake\n').lower()
    if choice_2 == "wait":
         choice_3=input("you have arrived at the island unharmed,"
               "there is a house with 3 doors"
               ".one red one yellow and one blue"
               " which colour do you choose\n")
         if choice_3=="red":
             print('you were burned by fire,GAME OVER')
         elif choice_3=="yellow":
             print("You have found the treasure,You have won the game")
         elif choice_3=="blue":
             print('you have entered room full of beasts,GAME OVER')
         else:
             print("You have chosen the door which doesn't exist get some help bro")
    else:
        print("you got attacked my crocodile's,Game over")
else:
    print("you have fell into the hole")




