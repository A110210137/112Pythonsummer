from stanfordkarel import *
import os

def invert_beepers():
     if beepers_present():
        pick_beeper()
     else:
          put_beeper()


def main():
    """ Karel code goes here! """
    while front_is_clear():
        if beepers_present():
            pick_beeper()
        else:
            put_beeper()
        move()

    if beepers_present():
            pick_beeper()
    else:
         put_beeper()

    pass

if __name__ == "__main__":
    run_karel_program(os.path.join(os.getcwd(), 'worlds/karel_09'))