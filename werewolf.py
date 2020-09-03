#!/usr/bin/env python
# coding: utf-8

# In[ ]:
############################################################################
#using random function
import random

############################################################################
##############                global variable                ###############
##############                                               ###############
############################################################################
#assigning the name of player
#if players array is empty program will ask user to input names

Players = []
#Players = ['Bee', 'Peter', 'Apple', 'Banana', 'cat', 'dog', 'dog', 'dog']

#default special char
#     index   0       1       2        3       4          5     
Chars = ['Werewolf','Seer','Hunter','Witch','Knight','Villager']

#variable for maximun players
Max_player = 100

#set the profiles for difference number of player
#the range is the range of number of player
#range(a, b) -> a >= x > b

#the string after the range is the index of special char
#e.g. "0012" -> Werewolf, Werewolf, Seer, Hunter
#     "000123" -> Werewolf, Werewolf, Werewolf, Seer, Hunter, Witch
Profile = {range(6,8) : "0012",
           range(8,11) : "000123",
           range(11, Max_player) : "00001234"}

############################################################################
##############                input user names               ###############
##############                                               ###############
############################################################################
#if no player name has set on Players's list at beginning

if(len(Players) == 0):
    #this while loop will loop forever until it break
    while(True):
        name = input("type the name of user {}\nor type \'skip\' to end the input\n".format(len(Players)+1))
        if(name.strip().lower() != 'skip'):
            Players.append(name)
        else:
            #break the while loop
            break
        
############################################################################
##############                start running                  ###############
##############                                               ###############
############################################################################
        
#this game must have at least 6 people to play
if len(Players) >= 6:
    #set the empty array of temp_assign_char
    temp_assign_char = []
    
    #find the profile that the 'lenth of players' is in the range of profile
    #the profile has set in beginning
    #Key is the Profile's range (e.g. range(6,8))
    for Key in Profile:
        #check if the 'lenth of players' is in the range of profile
        if len(Players) in Key:
            #using for loop to read all the string one by one
            #e.g. "0012"
            #it will for loop 0, 0, 1, 2
            #each time i will one of store 0, 0, 1, 2
            #and store it in the temp_assign_char array
            for i in range(len(Profile[Key])):
                temp_assign_char.append(int(Profile[Key][i]))
                
    ############################################################################
    #the real assign_char for the random use
    assign_char = []

    #loop the temp_assign_char that assigned just before
    #and use Chars[x] get the name of charater and store it to 'assign_char'
    for x in temp_assign_char:
        assign_char.append(Chars[x])

    #the remaining number of player get 'Villager' (index 5)
    for x in range(len(Players) - len(assign_char)):
        assign_char.append(Chars[5])

    #random the board
        #you can choose random 'Players' or 'assign_char'
        #it will not affect a lot
        #I think random Players will get beautifuler looks
    random.shuffle(Players)

    #finally display all players and assigned char
    for x in range(len(Players)):
        print('{}: {}'.format(Players[x], assign_char[x]))
else:
    print("""this game must have at least 6 people to play!
please restart this and input again:)""")

#keep window at last
input()

# In[ ]:




