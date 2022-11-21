# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 16:43:06 2021

@author: wajee
"""

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

rps_dictionary={0:rock, 1:paper, 2:scissors}


replay=1

while replay==1:
    
    computer_choice=random.randint(0, 2)

    player_choice=int(input('Select 0 for Rock, 1 for Paper or 2 for Scissors:'))
    
    if (player_choice > 2):
    
        print("Please select as per given choices")
    
    else: 
    
        if(player_choice==computer_choice):
            
            print('Player Chose')
            print(rps_dictionary[player_choice])
            print('Computer Chose')
            print(rps_dictionary[computer_choice])
            print('The Match is a draw')
        
        elif (player_choice != computer_choice):
            
            if (player_choice == 0):
                
                if (computer_choice==1):
                    
                    print('Player Chose')
                    print(rps_dictionary[player_choice])
                    print('Computer Chose')
                    print(rps_dictionary[computer_choice])
                    print('Computer Wins')
                
                elif (computer_choice==2):
                    
                    print('Player Chose')
                    print(rps_dictionary[player_choice])
                    print('Computer Chose')
                    print(rps_dictionary[computer_choice])
                    print('Player Wins')
                    
            if (player_choice == 1):
                
                if (computer_choice==0):
                    
                    print('Player Chose')
                    print(rps_dictionary[player_choice])
                    print('Computer Chose')
                    print(rps_dictionary[computer_choice])
                    print('Player Wins')
                
                elif (computer_choice==2):
                    
                    print('Player Chose')
                    print(rps_dictionary[player_choice])
                    print('Computer Chose')
                    print(rps_dictionary[computer_choice])
                    print('Computer Wins')
                    
            if (player_choice == 2):
                
                if (computer_choice==0):
                    
                    print('Player Chose')
                    print(rps_dictionary[player_choice])
                    print('Computer Chose')
                    print(rps_dictionary[computer_choice])
                    print('Computer Wins')
                
                elif (computer_choice==1):
                    
                    print('Player Chose')
                    print(rps_dictionary[player_choice])
                    print('Computer Chose')
                    print(rps_dictionary[computer_choice])
                    print('Player Wins')
                    
    replay=int(input('Do you want to keep playing press 1 for Yes 0 for No:'))   
       
  
  
        
        



