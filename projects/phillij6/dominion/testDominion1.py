# -*- coding: utf-8 -*-
"""
Created on 1/13/2020

@author: phillij6 (Justin Phillips)
"""

import Dominion
import random
import testUtility
from collections import defaultdict

#Get player names
player_names = ["*Annie","*Ben","*Carla"]

#number of curses and victory cards
if len(player_names)>2:
    nV=12
else:
    nV=8
nC = -10 + 10 * len(player_names)

#Define box
box = testUtility.GetBoxes(nV)

supply_order = testUtility.supplyOrder()

#Pick 10 cards from box to be in the supply.

supply = testUtility.randSupply(box)


#The supply always has these cards
#changed the supply of copper, silver, and gold to 0 to see the bug created
supply["Copper"]=[Dominion.Copper()]*(60-len(player_names)*0)
supply["Silver"]=[Dominion.Silver()]*0
supply["Gold"]=[Dominion.Gold()]*0
supply["Estate"]=[Dominion.Estate()]*nV
supply["Duchy"]=[Dominion.Duchy()]*nV
supply["Province"]=[Dominion.Province()]*nV
supply["Curse"]=[Dominion.Curse()]*nC

#initialize the trash
trash = []

#Costruct the Player objects
players = testUtility.playerFun(player_names)

#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score

dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)

