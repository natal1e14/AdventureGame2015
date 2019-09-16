#Natalie Ashgriz & Abby Tien (Full)
#Text Based Adventure Game
#November 26, 2015
#This game will ask the user a series of questions, where their choices/inputs
#will decide if they live or get caught and die.

import random

#Introduction & How-to
print "Welcome to the Woods! You were camping, but now your new friends have decided"
print "to change plans by playing a real life game of manhunt. You are being hunted"
print "inside an enclosed camping ground. You need to get out or find a safe place until morning"
print
print "To do this, you will answer a series of questions either Yes, No, Backward, Forward, Left, Right"
print "unless other options are given."
print "You may also take out and use objects by typing them in at any point."
print "Good luck!"
print


direction = raw_input("Which way do you want to go? ")
direction = direction.lower()

#If initial direction is Right
if direction == "right":
    direction2 = raw_input("Which way do you want to go now? ")
    if direction2 == "right":
        berries = raw_input("You find berries. Do you want to eat them? ")
        berries = berries.lower()
        if berries == "yes" or berries == "eat berries" or berries == "eat them":
            print "They were poisonous. You die!"
            print "GAME OVER"
        elif berries == "no":
            print "You find an opening in the fence and run out! You win!"
        else:
            print "That wasn't a choice. GAME OVER!"
    elif direction2 == "left":
        person = raw_input("You see somebody. Do you want to approach them or run away? ")
        person = person.lower()
        if person == "approach" or person == "approach them":
            print "The person was violent and stronger than you. You die."
            print "GAME OVER"
        elif person == "run" or person == "run away" or person == "runs away":
            direction3 = raw_input("Which way do you want to run? ")
            direction3 = direction3.lower()
            if direction3 == "forward" or direction3 == "forwards":
                print "You run into them! You lose!"
                print "GAME OVER"
            elif direction3 == "right":
                print "You run into a trap! You die!"
                print "GAME OVER"
            elif direction3 == "backward" or direction3 == "backwards":
                print "There is no going back! You are too cowardly."
                print "GAME OVER"
            elif direction3 == "left":
                enter = raw_input("You find an abandoned warehouse. Do you want to enter? ")
                enter = enter.lower()
                if enter == "yes" or enter == "y" or enter == "enter":
                    print "It's a trap! You lose!"
                    print "GAME OVER"
                elif enter == "no" or enter == "n" or enter == "don't enter":
                    climb = raw_input("You see a tree. Do you want to climb it? ")
                    climb = climb.lower() 
                    if climb == "yes" or climb == "y" or climb == "climb" or climb == "climb tree":
                        print "You get struck by lightning and die."
                        print "GAME OVER"
                    elif climb == "no" or climb == "n" or climb == "don't climb":
                        print "You stay sheltered at the base of the tree until morning."
                        print "You win!"
                    else:
                        print "That wasn't a choice. GAME OVER!"
                else:
                    print "That wasn't a choice. GAME OVER!"
            else:
                print "That wasn't a choice. GAME OVER!"
        else:
            print "That wasn't a choice. GAME OVER!"
    elif direction2 == "forward" or direction2 == "forwards":
        climb2 = raw_input("You see a tree. Do you want to climb it? ")
        climb2 = climb2.lower()
        if climb2 == "yes" or climb2 == "y" or climb2 == "climb" or climb2 == "climb tree":
            strength = random.randint(0,100)
            if strength >= 50:
                eat2 = raw_input("You climb the tree. There is an apple. Do you want to eat it? ")
                eat2 = eat2.lower()
                if eat2 == "yes" or eat2 == "y" or eat2 == "eat apple" or eat2 == "eat" or eat2 == "eat it":
                    print "The apple was booby-trapped. You are caught!"
                    print "GAME OVER"
                elif eat2 == "no" or eat2 == "n" or eat2 == "don't eat it" or eat2 == "don't eat apple":
                    print "Good choice. You wait in the tree until morning."
                    print "You win!"
                else:
                    "That wasn't a choice. GAME OVER!"
            elif strength < 50:
                print "You are too weak and fall to your death!"
                print "GAME OVER"
            else:
                print "That wasn't a choice. GAME OVER!"
        elif climb2 == "no" or climb2 == "n" or climb2 == "don't climb" or climb2 == "don't climb tree":
            print "You run into someone and die."
            print "GAME OVER"
        else:
            print "That wasn't a choice. GAME OVER!"
    elif direction2 == "backward" or direction2 =="backwards":
        setup = raw_input("You find a camping kit. Do you want to set it up? ")
        setup = setup.lower()
        if setup == "yes" or setup == "y" or setup == "set it up" or setup == "set up camp":
            print "They hear you! You die!"
            print "GAME OVER"
        elif setup == "no" or setup == "n" or setup ==  "don't set it up":
            setup2 = raw_input("It starts raining. Do you want to set up camp now? ")
            setup2 = setup2.lower()
            if setup2 == "yes" or setup2 == "y" or setup2 == "set up camp":
                print "You evade caputre and the cold. You win!"
            elif setup2 == "no" or setup2 == "n" or setup2 == "don't set up camp":
                print "You die of hypothermia."
                print "GAME OVER"
            else:
                print "That wasn't a choice. GAME OVER!"
        else:
            print "That wasn't a choice. GAME OVER!"
    else:
        print "That wasn't a choice. GAME OVER!"

#If initial direction is Backward
elif direction == "backward" or direction =="backwards":
    direction4 = raw_input("You hit a fence. Which way do you want to go? ")
    direction4 = direction4.lower()
    if direction4 == "backward" or direction4 == "backwards":
        print "You step into a net. They are coming for you! You lose!"
        print "GAME OVER"
    elif direction4 == "forward" or direction4 == "forwards":
        climb3 = raw_input("Do you want to climb the fence? ")
        climb3 = climb3.lower()
        if climb3 == "yes" or climb3 == "y" or climb3 == "climb fence":
            print "It's an electric fence! You die!"
            print "GAME OVER"
        elif climb3 == "no" or climb3 == "n" or climb3 == "don't climb fence":
            print "You see a light behind you. They have found you."
            print "You lose. GAME OVER"
        else:
            print "That wasn't a choice. GAME OVER!" 
    elif direction4 == "right" or direction4 == "left":
        pickUp = raw_input("You feel something. Do you want to pick it up? ")
        pickUp = pickUp.lower()
        if pickUp == "yes" or pickUp == "y" or pickUp ==  "pick it up":
            flashlight = raw_input("You find a flashlight. Turn it on? ")
            flashlight = flashlight.lower()
            if flashlight == "yes" or flashlight == "y" or flashlight == "turn it on":
                print "They see you. You lose!"
                print "GAME OVER"
            elif flashlight == "no" or flashlight == "n" or flashlight == "don't turn it on":
                danger = raw_input("You hear something. It could be them. Do you want to run or walk away? ")
                danger = danger.lower()
                if danger == "walk" or danger == "walk away":
                    flashlight2 = raw_input("Good choice. Do you want to turn on the flashlight now? ")
                    flashlight2 = flashlight2.lower()
                    if flashlight2 == "yes" or flashlight2 == "y" or flashlight2 == "turn it on":
                        print "In the light, you see a tree leaning over the fence and escape!"
                        print "You win!"
                    elif flashlight2 == "no" or flashlight2 == "n" or flashlight2== "don't turn it on":
                        print "It's too dark! You fall and they catch you!"
                        print "GAME OVER"
                    else:
                        print "That wasn't a choice. GAME OVER!"
                elif danger == "run" or danger == "run away":
                    print "You were too loud and were caught!"
                    print "GAME OVER"
                else:
                    print "That wasn't a choice. GAME OVER!"
            else:
                print "That wasn't a choice. GAME OVER!"
        elif pickUp == "no" or pickUp == "n" or pickUp == "don't pick it up":
            direction5 = raw_input("Which way do you want to go now? ")
            direction5 = direction5.lower()
            if direction5 == "left":
                print "You step into a net. They are coming. You lose!"
                print "GAME OVER"
            elif direction5 == "right":
                stepInTrap = random.randint(0,100)
                if stepInTrap >= 50:
                    print "You step in a trap and are caught. You lose."
                    print "GAME OVER"
                elif stepInTrap < 50:
                    wolf = raw_input("A wolf approaches you. Do you want to confront it or run away? ")
                    if wolf == "confront":
                        print "You are too weak. The wolf eats you."
                        print "GAME OVER"
                    elif wolf == "run away":
                        print "The wolf is faster than you. He attacks you."
                        print "GAME OVER"
                    else:
                        print "That wasn't a choice. GAME OVER!"
                else:
                    print "That wasn't a choice. GAME OVER!"
            elif direction5 == "forward" or direction5 == "forwards":
                pickUp2 = raw_input("You feel something. Do you want to pick it up? ")
                pickUp2 = pickUp2.lower()
                if pickUp2 == "yes" or pickUp2 == "y" or pickUp2 == "pick it up":
                    umbrella = raw_input("You got an umbrella. Do you want to use it? ")
                    umbrella = umbrella.lower()
                    if umbrella == "y" or umbrella == "yes" or umbrella == "use it" or umbrella == "use umbrella":
                        print "While opening the umbrella, you stab yourself in the eye and are blinded."
                        print "You lose. GAME OVER"
                    elif umbrella == "no" or umbrella == "n" or umbrella == "don't use it":
                        rain = raw_input("It starts to rain. Do you want to use the umbrella now? ")
                        rain = rain.lower()
                        if rain == "yes" or rain == "y" or rain == "use umbrella" :
                            print "Good choice. Without rain in your eyes, you spot a way out."
                            print "You win!"
                        elif rain == "no" or rain == "n" or rain == "don't use umbrella":
                            print "The rain is too hard. You cannot see and are soaking wet."
                            print "You get hypothermia and run into them. You lose."
                            print "GAME OVER"
                        else:
                            print "That wasn't a choice. GAME OVER!"
                    else:
                        print "That wasn't a choice. GAME OVER!"
                elif pickUp2 == "no" or pickUp2 == "n" or pickUp2 == "don't pick up":
                    print "It starts to rain and you are struck by lightning. You die"
                    print "GAME OVER"
                else:
                    print "That wasn't a choice. GAME OVER!"
            elif direction5 == "backward" or direction5 == "backwards":
                print "There is no going back, you coward!!!"
                print "You are not worthy of continuing! GAME OVER"
            else:
                print "That wasn't a choice. GAME OVER"
        else:
            print "That wasn't a choice. GAME OVER"
    else:
        print "That wasn't a choice. GAME OVER"
    
#if choose to go left
elif direction == "left":
    q1 = raw_input("Are you scared yet? ")
    q1 = q1.lower()
    print
    
    #if they are scared
    if q1=="yes":
        q2 = raw_input("Good, which way do you want to go now? ")
        q2 = q2.lower()
        print
        if q2=="right" or q2=="left":
            print "Oh no! You just walked into your friends. \nGAME OVER."
        elif q2=="forward" or q2=="backward":
            q3 = raw_input("You trip over a metalic mass on the ground. Do you wish to pick it up? ")
            q3 = q3.lower()
            print
            
            #Pick up a bear trap
            if q3=="yes":
                print "It's a bear trap. You are caught. \nGAME OVER."
            
            #Do not and go into clearing
            elif q3=="no":
                q4 = raw_input("Thats a good choice. You see a clearing ahead, do you want to walk into it? ")
                q4 = q4.lower()
                print
                if q4=="yes":
                    print "You are rescued by a helicopter. They had previous knowledge of the group and came to find you! \nYOU WIN!"
                elif q4=="no":
                    print "They were waiting in the woods. They catch you. \nGAME OVER."
                else:
                    print "That wasn't a choice. \nGAME OVER."
            else:
                print "That wasn't a choice. \nGAME OVER."
        else:
            print "That wasn't a choice. \nGAME OVER."
            
    #They are not scared
    elif q1=="no":
        q5 = raw_input("Too bad. You step on a paper on the ground. Do you wish to pick it up? ")
        q5 = q5.lower()
        print
        
        #They have gained a map
        if q5=="yes":
            map = 1
            q6 = raw_input("It's a map! Do you want to put it into your backpack? ")
            q6 = q6.lower()
            print
            
            #map is put in backpack
            if q6=="yes":
                    map = 2
                    q62 = raw_input("You keep walking, and step into a swamp. What or where do you want to do? ")
                    q62 = q62.lower()
                    print
                    if q62=="forward" or q62=="backward" or q62=="right":
                        print "You go further into the swamp, and get eaten by a monster fish. \nGAME OVER."
                    
                    #map is ruined in water 
                    elif q62=="left":
                        q63 = raw_input("You go further into the swamp, and are now neck deep in water. What do you want to do now? ")
                        q63 = q63.lower()
                        map = 3
                        print
                        if q63=="forward" or q63=="backward" or q63=="right" or q63=="left":
                            print "You swim into the electric fence. \nGAME OVER."
                        elif q63=="map":
                            if map==3:
                                print "Your map was ruined in the water. You are lost. \nGAME OVER."
                            elif map==1 or map==2:
                                print "You use your map to navigate yourself out. \nYOU WIN!"
                            else:
                                print "You don't have a map. That's not a choice. \n GAME OVER."
                        else:
                            print "That wasn't a choice. \nGAME OVER."
                    elif q62=="map":
                        if map==2 or map==1:
                            print "You take out your map and reorientate yourself using the swamp. You make it to the exit. \nYOU WIN!"
                        else:
                            print "You are lost. You don't have a map. \nGAME OVER."
                    else:
                        print "That wasn't a choice. \nGAME OVER."
                        
            #map is not in backpack
            elif q6=="no":
                q61 = raw_input("Do you want follow the map directly out? ")
                q61 = q61.lower()
                print
                if q61=="yes":
                    chance1 = random.randint(1,100)
                    if chance1<=50:
                        print "You had a {}% chance of getting out without getting caught, so you were caught. \nGAME OVER.".format(chance1)
                    else:
                        print "You had a {}% chance of getting out without getting caught, so you got out! \nYOU WIN!".format(chance1)
                elif q61=="no":
                    print "You keep going, and use the map as needed. You make it out. \nYOU WIN!"
            
            #keep looking at map
            elif q6=="map":
                print "You keep examining your map, but are ambushed by your friends. \nGAME OVER." 
            else:
                    print "That wasn't a choice. \nGAME OVER."
        
        #you do not have a map            
        elif q5=="no":
            print "You are lost and get caught. Too bad you missed out on the map! \nGAME OVER."
        else:
            print "That wasn't a choice. \nGAME OVER."
    else:
        print "That wasn't a choice.\nGAME OVER."
                 
#if choose to go forwards
elif direction=="forward":
    q7 = raw_input("You kick something at your feet. Do you wish to pick it up? ")
    q7 = q7.lower()
    print
    
    #have a knife
    if q7=="yes":
        q8 = raw_input("It's a knife! Do you want to put it into your backpack? ") 
        q8 = q8.lower()
        knife = 1
        print
        
        #knife in backpack
        if q8=="yes":
            knife = 2
            q81 = raw_input("Which way do you want to go? ")
            q81 = q81.lower()
            print
            if q81=="right" or q81=="left":
                q9 = raw_input("You have run into one of your friends! Do you want to stay and fight? ")
                q9 = q9.lower()
                print
                if q9=="yes":
                    chance2 = random.randint(1,100)
                    if chance2>=50:
                        print "You were stronger than your attacker by {}%! \nYOU WIN!".format(chance2)
                    else:
                        print "You were weaker than your attacker by {}%. \nGAME OVER.".format(chance2)
                elif q9=="no":
                    print "You tried to run away, but they were faster. \nGAME OVER."
                elif q9=="knife":
                    if knife==2:
                        print "You take the knife out of your backpack. You use it to fight your attacker. \nYOU WIN!"
                else:
                    print "That wasn't a choice. \nGAME OVER."
            elif q81=="forward" or q81=="backward":
                print "You walk into the electric fence. \nGAME OVER."
            else:
                print "That wasn't a choice. \nGAME OVER."
        
        #knife not in backpack
        elif q8=="no":
            q82 = raw_input("Which way do you want to go? ")
            q82 = q82.lower()
            print
            if q82=="forward" or q82=="backward":
                if knife==1:
                    print "You tripped over a rock and stabbed yourself. \nGAME OVER."
                if knife==2:
                    print "You run into the electric fence. \nGAME OVER."
            elif q82=="right" or q82=="left":
                if knife==2:
                    print "You see your friends, but don't have your knife out. \nGAME OVER."
                if knife==1:
                    print "You see your friends, and fight them with your knife. \nYOU WIN!"
        
        #use knife
        elif q8=="knife":
            print "You examine your knife and cut yourself. \nGAME OVER."
        else:
            print "That wasn't a choice. \nGAME OVER."
    
    #do not pick up knife
    elif q7=="no":
        q10 = raw_input("You hear somebody. Do you want to stick around to see who it is? ")
        q10 = q10.lower()
        print
        
        #stay to see who is there
        if q10=="yes":
            print "You get caught and can't escape. Too bad you missed out on that knife! \nGAME OVER."
        
        #leave the area instead
        elif q10=="no":
            chance3 = random.randint(1,3)
            if chance3==1:
                print "You just evaded capture. Unfortuneately while you were running you ran right into the electric fence. \nGAME OVER."
            elif chance3==2:
                print "You just evaded capture. Unfortuneately it was short lived because your friends were surrounding you. They caught you. \nGAME OVER."
            elif chance3==3:
                q11 = raw_input("You evaded capture and run into a clearing. You then stumble on something. Do you want to pick it up? ")
                q11 = q11.lower()
                if q11=="yes":
                    print "It's a map. You use it to run out! \nYOU WIN!"
                elif q11=="no":
                    print "You are now lost. You are wandering helplessly and get caught. Too bad you missed the map! \nGAME OVER."
                else:
                    print "That wasn't a choice. \nGAME OVER."
        else:
            print "That wasn't a choice. \nGAME OVER."
    else:
        print "That wasn't a choice. \nGAME OVER."

#if enter an invalid direction
else:
    print "That wasn't a choice. \nGAME OVER."
        


    
            




