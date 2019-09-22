'''
Displays the battle UI
'''
import time
import os
from queue import Queue
import threading
from curtsies import Input

class PlayerTurnUI():

    def __init__(self):
        self.q = Queue()
        self.possible_actions = [self.hover_on_attack, self.hover_on_skill,
                                 self.hover_on_guard, self.hover_on_item,
                                 self.hover_on_flee]

        self.show_UI("Phillip")

    def show_UI(self, character_name:str):
        print("It's " + character_name + "'s Turn!")
        choice = 0
        key_listener = threading.Thread(target=self.listen_for_input_and_space)
        key_listener.start()

        while True:
            os.system('cls' if os.name == 'nt' else 'clear') # clear the temrnial
            if(not self.q.empty()):
                dir = self.q.get()
                if(dir == 'UP'):
                    choice = max(0, choice - 1)
                elif(dir == 'DOWN'):
                    choice = min(4, choice + 1)


            self.possible_actions[choice]()
            while(self.q.empty()):
                continue



    def hover_on_attack(self):
        '''
        Display menu with cursor hovering on attack
        '''
        print("---> Attack\n     Skill\n     Guard\n     Item\n     Flee\n",end="\r")


    def hover_on_skill(self):
        '''
        Display menu with cursor hovering on skill
        '''
        print("     Attack\n---> Skill\n     Guard\n     Item\n     Flee\n",end="\r")

    def hover_on_guard(self):
        '''
        Display menu with cursor hovering on guard
        '''
        print("     Attack\n     Skill\n---> Guard\n     Item\n     Flee\n",end="\r")

    def hover_on_item(self):
        '''
        Display menu with cursor hovering on item
        '''
        print("     Attack\n     Skill\n     Guard\n---> Item\n     Flee\n",end="\r")

    def hover_on_flee(self):
        '''
        Display menu with cursor hovering on flee
        '''
        print("     Attack\n     Skill\n     Guard\n     Item\n---> Flee\n",end="\r")

    def listen_for_input_and_space(self):
        '''
        This is a threaded function that will be called by
        the 'display_text' method. It will listen for the user
        entering a space and will either continue to the next
        line of text or finish the scrolling effect on the
        current line of text
        '''
        with Input(keynames='curses') as input_generator:
            for e in input_generator:
                if(e == 'KEY_UP'):
                    self.q.put("UP")
                elif(e == 'KEY_DOWN'):
                    self.q.put("DOWN")
                if(e == ' '):
                    self.q.put(0)
