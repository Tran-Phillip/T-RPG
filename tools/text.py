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
q = Queue()
q.put(1)
def input_listener():
    with Input(keynames='curses') as input_generator:
        for e in input_generator:
            if(q.empty()):
                sys.exit(1)
            if(e == ' '):
                q.get()



def text(text_to_display:str):
    '''
    This will be used when a user wants to display text in the game.
    Use this as opposed to print because text will format text and scroll through
    it in a 'video-game' like manner

    :param text_to_display: The text you want to display...?
    :type text_to_display: python string

    :return: None, but displays the text on the screen.
    '''

    x = threading.Thread(target=input_listener)
    x.start()
    for character in text_to_display:
         sys.stdout.write(character) #  Having buffer issues when using print(..., end='')
         sys.stdout.flush()
         if(not q.empty()):
             time.sleep(0.25)
    if(not q.empty()):
        q.get()
    print("")
