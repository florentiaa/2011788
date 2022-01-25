print("====== Through The Unknown ======")
print("")

#create list for inventory items
inventory = ["dagger", "small potion"]

#using append in order to add more items in the inventory
def addToInventory(item):
    inventory.append(item)
print("Your inventory:", inventory)

#defing the health variables of the characters
enemy_hp = 20
myhealth = 100

answer = input("Would you like to play? yes/no: ")

if answer.lower().strip() == "yes":

    print("")
    # input player's name
    name = input("Enter your name: ")
    print("")
    print(name, ",your spaceship has crashed on an unknown planet.")
    print("None of your crew mates have survived and you are the only one left.")
    print("You now need to find you way back home and survive the colonies while exploring your surroundings.")
    print("")
    print("You take your first step outside the ship.\nAfter a while you see a portal appear next to you.")
    print("Your inventory:", inventory)
    answer = input("Do you want to take the portal? ").lower().strip() #making the input readable in case of accidental capital letters
    if answer == "yes":
        print("")
        print(name, ",you found yourself new inventory items!")
        print("You found a grenade, an orbit gun and a medkit!")
        addToInventory("grenade") #adding the new items in the inventory
        addToInventory("orbit gun")
        addToInventory("medkit")
        print("")
        print("Your inventory:", inventory) #displaying the new inventory
        print("")
        print("A few miles later you hear a strange sound coming from behind you!")
        print("You slowly turn around... you have encountered a peculiar creature with odd features.")
        print("Beware as it might be dangerous! Gather your weapons and healing items.")
        answer = input("The monster is attacking you! Do you run or attack? attack/run: ")
        if answer == "attack":
            print("")
            print(inventory)
            print("")
            answer = input("What are you attacking it with? ") #according to player's choice of weapon the enemy and the player will lose a different percentage of HP
            if answer == "dagger":

                print("You just killed the monster!But you lost 50 of you health!")
                print("")

                myhealth -= 50
                enemy_hp -= 20
                print("Monsters HP:", enemy_hp)  # printing enemy's health and the player's
                print("My Health:", myhealth)
                print("")
            elif answer == "orbit gun":

                print("You just killed the monster! But you lost 50 of you health!")
                myhealth -= 50 #printing enemy's health and the player's
                enemy_hp -= 20
                print("")
                print("Monsters HP:", enemy_hp)
                print("My Health:", myhealth)
                print("")
            elif answer == "grenade":
                print("You just killed the monster! But you lost 50 of you health!")
                myhealth -= 50
                enemy_hp -= 20
                print("")
                print("Monsters HP:", enemy_hp)  # printing enemy's health and the player's
                print("My Health:", myhealth)
                print("")
            answer = input("Do you want to use your medkit now? ")
            if answer == ("yes"):
                myhealth += 50 #player healing using the medkit
                print("")
                print("My Health:", myhealth)
                print("")
                print("You just walked a few more miles and you finally see a colony of human-like Aliens.")
                answer = input("You have to talk to them in order to survive. Are you friendly with them or not? ")
                if answer == ("yes"):
                    print("")
                    print("The Aliens give you food, new clothes and they helped you to contact earth to send help.")
                    print("A few months have pasted and you made new friends,\nyou have a job and your life is as good as it was back home on Earth.")
                    print("NASA will have their spaceship there by the end of the month.")
                    answer = input("Are you going back to Earth or are you staying there? stay/leave: ")
                    if answer == "stay":
                        print("Nasa respects your decision \nand awards you for you patience and for making allies with your own spaceship to return whenever you want!")
                    else:
                        print("Even thought the Aliens were sad they respect your decision and they can't wait to see you again!")
                else:
                        print("You approached them very aggresivly and you scared them. Now they are keeping you as a hostage. GAME OVER! ")
            else:
                print("After a few more miles the injuries got worse and you died in the middle of the planet.")
        else:
            print("You just fell in a hole and died..")
    elif answer == "no":
        print("A giant Clawheaded Monster just attacked you from the back... Game Over.")

else:
    print("Well that's to bad!")