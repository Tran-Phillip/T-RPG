# Author(s): Phillip Tran

'''
This file will contain functions pertaining to how text is
displayed on the screen and the modification / usage of text
'''
# first party
import time
import sys
#print("Progress {}".format("test" + character), end="\r")
import threading
from curtsies import Input
from queue import Queue


class Text:

    def __init__(self, text:str):
        '''
        This will be used when a user wants to display text in the game.
        Use this as opposed to print because text will format text and scroll through
        it in a 'video-game' like manner

        :param text: The text you want to display...?
        :type text_to_display: python string

        :return: None, but displays the text on the screen.
        '''
        self.q = Queue() # used to communicate between threads
        self.q.put(1) # We use an element in the queue to determine whether or not the text is still being displayed
        self.display_text(text)

    def listen_for_space(self):
        '''
        This is a threaded function that will be called by
        the 'display_text' method. It will listen for the user
        entering a space and will either continue to the next
        line of text or finish the scrolling effect on the
        current line of text
        '''
        with Input(keynames='curses') as input_generator:
            for e in input_generator:
                if(self.q.empty()):
                    sys.exit(1)
                if(e == ' '):
                    self.q.get()

    def display_text(self,text:str):
        '''
        Displays text on the screen and includes a little scrolling effect
        '''
        listener = threading.Thread(target=self.listen_for_space)
        listener.start()
        c_count = range(1,len(text) + 1)
        for character, pos in zip(text, c_count):
             sys.stdout.write(character) #  Having buffer issues when using print(..., end='')
             sys.stdout.flush()
             if(pos % 80 == 0):
                 print("")
             if(not self.q.empty()):
                 time.sleep(0.25)
        if(not self.q.empty()):
            self.q.get()
        print("")
        listener.join()
