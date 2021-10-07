# -*- coding: utf-8 -*-
"""
P A T S
a text-based game played in command prompt
raise virtual pets! 
pat them! euthanize them! feed them! 

everything you can do to a real pet!! 

Last edited 7 October 2021 by Caitlin Chung
"""
import time
import random

class Person(object):
    """
    Each entry is for one person. Each person has their own stats for their
    pet. Here is where it is stored.
    """
    def __init__(self,s,pn,h,ha,tob,t):
        """
        stores info about pets
        """
        self.species = s
        self.petname = pn
        self.health = h
        self.happiness = ha
        self.time_of_birth = tob #never change
        self.time_of_last_visit = t
        
def first_pet():
    time.sleep(.5)
    print("I'll get my zoo catalog out just for you!\n")
    time.sleep(.5)
    print("Alright, so type the number next to an animal name to select your pet!")
    time.sleep(.5)
    catalog = {1:["Cat",100,50],2:["Dog",100,70],3:["Dragon",150,20],\
               4:["Ferret",30,40],5:["Horse",110,40]}
    chosen = ""
    animal = ""
    healthy = 0
    happy = 0
    choose = ""
    
    print("Species|Health|Starting Happiness")
    string = ""
    listed = []
    for selection in catalog:
        string += str(selection) + ") "
        listed.append(selection)
        for x in catalog[selection]:
            string += str(x) + "|"
        string += "\n"
    print(string)
    
    while chosen != "yes" or choose.lower() != "cancel":
        choose = input("So? What'll it be, mate?\n>> ")
        choose = int(choose)
        if choose in listed:
            chosen = "yes"
            animal = catalog[choose][0]
            healthy = catalog[choose][1]
            happy = catalog[choose][2]
            break
        else:
            print("That is an invalid response! Try again!")
    time.sleep(.5)
    print("Wow, crikey, look at 'em! What a beaut!")
    time.sleep(.5)
    petname = input("What would you like to name 'em?\n>> ").title()
    time.sleep(.5)
    print("{}, gorgeous name! Thanks for stopping by!".format(petname))
    return [animal,petname,healthy,happy]

def save_file(petlog):
    f = open("Desktop\PAT_FILE.txt",'w')

    petstrh = ""
    del petlog["0"]
    for thing in petlog:
        #for pet in petlog[person]:
        count = 0
        for x in petlog[thing]:
            count += 1
        for x in range(0,count):
            petstrh += "{}|{}|{}|{}|{}|{}|{}\n\n".format(thing,str(petlog[thing][x].species)\
                        ,str(petlog[thing][x].petname),str(petlog[thing][x].health),\
                        str(petlog[thing][x].happiness),str(petlog[thing][x].time_of_birth),\
                        str(petlog[thing][x].time_of_last_visit))
    f.write(petstrh)
    f.close()
    
def open_file():
    #opening file
    f = open('Desktop\PAT_FILE.txt')
    file = f.read()
    
    all_lines = ""
    all_lines += "0|0|0|0|0|0|0\n\n"
    for line in file:
        all_lines += str(line)
    all_entry = all_lines.strip().split("\n\n")
    
    for x in range(len(all_entry)):
        all_entry[x] = all_entry[x].split("|")

    petlog = {}
    entry_list = list()
    for entry in all_entry:
        entry_list.append(Person(entry[1],entry[2],entry[3],entry[4],entry[5],entry[6]))
        if entry[0] in petlog: #if the person's name is there already,
            petlog[entry[0]].append(Person(entry[1],entry[2],entry[3],entry[4],entry[5],entry[6]))
        else:
            petlog[entry[0]] = [Person(entry[1],entry[2],entry[3],entry[4],entry[5],entry[6])]
    return petlog

##############################################33
petlog = open_file()
if len(petlog) > 1:
    x = ""
    print("New Player? Y or N")
    while x != "y" and x!= "n":
        x = input(">> ")
        x = x.lower()
        if x == "or":
            print("Hah, wise guy. Try again.\n")
        elif x == "y" or x == "n":
            break
        else:
            print("Sorry, that wasn't a valid answer. Please try again!")
            print("New Player? Y or N")
    #new user
    if x == "y":
        valid = False
        name = input("Oh, welcome! What's your name?\n>> ").title()
        while valid == False:
            if name in petlog.keys():
                print("\nSorry, that name is already taken.")
                name = input("Please choose another name!\n>> ").title()
            elif name == "Exit" or name == "Quit" or name == "Cancel":
                break
            else:
                print("\nWelcome, {}!".format(name))
                petlog[name] = list()
                valid = True
    #old user
    if x == "n":
        name = input("Please type in your username: \n>> ").title()
        valid = False
        while valid == False:
            if name not in petlog.keys():
                print("\nSorry, we don't recognize that username. Please try again!")
                name = input("Please type in your username: \n>> ").title()
            else:
                valid = True
                print("\nWELCOME BACK, {}".format(name.upper()))
                break
else: #brand new save
    entry_list = list()
    print("Hello and welcome, New Player!")
    name = input("What's your name?\n>> ").title()
    valid = False
    while valid == False:
        if name == "0":
            print("\nSorry, that name is already taken.")
            name = input("Please choose another name!\n>> ").title()
        else:
            print("\nWelcome, {}!".format(name))
            petlog[name] = list()
            valid = True
        
#happiness and health deductions
for pet in petlog[name]:
    time_since_last_visit = float(time.time())-float(pet.time_of_last_visit)
    days_since_last_visit = float(time_since_last_visit) / 86200 #a little less than actual, 86400
    happ = float(pet.happiness)
    heal = float(pet.health)
    happ -= max(0,round(days_since_last_visit))
    heal -= max(0.5, round(2 * days_since_last_visit))
    pet.happiness = str(happ)
    pet.health = str(heal)

to_go = ""
number = 0
dying = 0
depressed = 0
for pet in petlog[name]:
    number += 1
    if float(pet.health) <= 20:
        dying += 1
    if float(pet.happiness) <= 10:
        depressed += 1
if number == 0: #loners
    print("{}, you have 0 pets! What's life without a pet or two?\nLet's get a pet for you!".format(name.title()))
    new = first_pet()
    petlog[name] = [Person(new[0],new[1],new[2],new[3],time.time(),time.time())]
    save_file(petlog)
    petlog = open_file()
    
number = len(petlog[name])
if number == 1:
    print("{}, you have 1 pet!".format(name.title()))
    if dying != 1 and depressed != 1:
        print("Luckily for you, it's happy and healthy!")
    elif depressed == 1:
        print("Sadly, your pet {} is depressed".format(petlog[name][0].petname))
        if dying == 1:
            print("and dying. What type of pet owner are you?!")
        else:
            print("but it's not dead yet!")
    else:
        print("Amazingly, your pet {} is happy".format(petlog[name][0].petname))
        if dying == 1:
            print("but at death's door.")
        else:
            print("and healthy! What a great owner!")
if number > 1:
    print("{}, you have {} pets! Quite a zoo you've got there!".format(name.title(),number))
    if dying == 0 and depressed == 0:
        print("Congrats! None of your pets are dying nor depressed! (yet)")
while to_go != "Y":
    choose_your_fighter2 = ""
    while choose_your_fighter2 != "exit":
        time.sleep(1)
        print("Which of your pets would you like to interact with?")
        time.sleep(.5)
        choose_your_fighter = ""
        choose_your_fighter = "\n#|NAME|SPECIES|JOY LVL|HEALTH|LAST INTERACTION"
        qwerty = 0
        for x in range(0,len(petlog[name])):
            qwerty = x
            seconds_ago = round(time.time()-float(petlog[name][x].time_of_last_visit))
            if seconds_ago >= 1586189279:
                seconds_ago = "TEST FILE! THIS IS NOT YOUR PET WHY ARE YOU HERE"
            choose_your_fighter += "\n" + str(x) + "|{}|{}|{}|{}|{} seconds ago".format(str(petlog[name][x].petname),\
                                                 str(petlog[name][x].species),\
                                                  str(petlog[name][x].happiness),\
                                                   str(petlog[name][x].health),\
                                                   str(seconds_ago))                                                
        choose_your_fighter += "\n" + str(qwerty+1) + "|Adopt a New Pet\nEXIT"
        print(choose_your_fighter)
        time.sleep(.5)
        xx = ""
        while xx != "true":
            choose_your_fighter2 = input("Type the number of your selected pet to select it, or 'EXIT' to leave.\n>> ").lower()
            if choose_your_fighter2 == "exit":
                xx = "true"
                break
            elif petlog[name][x].species == "0":
                xx = "true"
                print("Why are you interacting with someone else's pets? Rude.")
                to_go = "Y"
                break
            elif choose_your_fighter2 == str(qwerty+1):
                new = first_pet()
                petlog[name].append(Person(new[0],new[1],new[2],new[3],time.time(),time.time()))
                xx = "true"
            elif int(choose_your_fighter2) <= qwerty and int(choose_your_fighter2) >= 0:
                chosenpet = petlog[name][int(choose_your_fighter2)]
                time_since_last_visit = float(time.time())-float(chosenpet.time_of_last_visit)
                days_since_last_visit = float(time_since_last_visit) / 86200
                print("This is {}, your {}! You adopted them {} hours ago!".format(chosenpet.petname,chosenpet.species,str(round((time.time() - float(chosenpet.time_of_birth))/3600,2))))
                print("You've last visited them {} days ago! Boy, are they happy to see you!".format(round(days_since_last_visit,1)))
                chosenpet.time_of_last_visit = time.time()
                chosenpet.happiness = str(float(chosenpet.happiness)+1)
                print("\n{}'s happiness went up by 1 and now stands at a solid {}!".format(chosenpet.petname,chosenpet.happiness))
                print("What would you like to do?\n1) Feed(+5 Health)\n2) Play(+3 Happiness)\n3) Euthanize\n")
                ii = False
                while ii != True:
                    interact = input("Type the number associated with your chosen action!\n>>")
                    if interact == str(1):
                        chosenpet.health = str(float(chosenpet.health)+5)
                        x = random.choice(["You threw a treat at them and they eagerly gobbled it up!",\
                                                 "You filled up their bowl with a nice helping of {} food. \nThey loved it!".format(chosenpet.species),\
                                                 "You tossed a whole bunch of their favorite food. They enjoyed it!"])
                        print(str(x))
                        print("Their health shot up by 5, landing at a grand total of {}!".format(chosenpet.health))
                        ii = True
                    elif interact == str(2):
                        chosenpet.happiness = str(float(chosenpet.happiness)+3)
                        x = random.choice(["You softly pet their head, and they enjoyed it!",\
                                                 "You threw their favorite toy and they happily chased after it!"])
                        print(str(x))
                        print("Their happiness shot up by 3, landing at a grand total of {}!".format(chosenpet.happiness))
                        ii = True
                    elif interact == str(3):
                        ee = False
                        while ee != True:
                            if len(petlog[name]) == 1:
                                print("Sorry, you can't perform this action. You only have one pet!\n\n")
                                ee = True
                                ii = True
                            elif len(petlog[name]) > 1:
                                print("{} looks at you with sad eyes.".format(chosenpet.petname))
                                uu = input("Are you sure you want to do this? Y/N\n>>").lower()
                                if uu == "n":
                                    ee = True 
                                    print("What would you like to do?\n1) Feed(+5 Health)\n2) Play(+3 Happiness)\n3) Euthanize\n")
                                    ii = True
                                elif uu == "y":
                                    print("The spark in {}'s eyes fade away. They close their eyes and breathe their last.".format(str(chosenpet.petname)))
                                    del petlog[name][int(choose_your_fighter2)]
                                    
                                    number -= 1
                                    ee = True
                                    ii = True
                                    xx = True
                            ee = True

                xx = "true"
            else:
                print("Sorry, invalid response. Please try again.")
            
    to_go = input("\nAre you sure you want to exit? Y/N\n").title()

save_file(petlog)
