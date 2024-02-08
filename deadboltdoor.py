import door
import random

class DeadboltDoor(door.Door):
  '''Creates a locked door with two bolts that need to be unlocked
   Attributes:
   1.choices for the state of each bolt(locked or unlocked)
   2.List of choices for the state of the door
  '''

  def __init__(self):
    '''Initializes variables'''
    self.choices = ['Toggle bolt 1', 'Toggle bolt 2']
    bolt_states = ['locked', 'unlocked']
    self._bolt_1_state = random.choice(bolt_states)
    self._bolt_2_state = random.choice(bolt_states)

  def examine_door(self):
    '''Returns a string description of the door'''
    return 'A door with two deadbolts. Both need to be unlocked to open the door, but you can\'t tell if each one is locked or unlocked.'

  def menu_options(self):
    '''returns a string of the menu options that user can choose from when attmpting to unlock the door'''
    menu_options = ''
    for i, choice, in enumerate(self.choices):
      menu_options += f'{i + 1}. {choice}\n'
    return menu_options

  def get_menu_max(self):
    '''returns the number of options in the above menu'''
    return 2

  def attempt(self, option):
    '''passes in the user's selection from the menu. Uses that value to update the attributes that are needed to determine whether the user has unlocked the door. Return a string describing what the user atttempted'''
    if option == 1:
      if self._bolt_1_state == 'unlocked':
        self._bolt_1_state = 'locked'
      else:
        self._bolt_1_state = 'unlocked'
    else:
      if self._bolt_2_state == 'unlocked':
        self._bolt_2_state = 'locked'
      else:
        self._bolt_2_state = 'unlocked'
    return f'You {self.choices[option - 1].lower()}'

  def is_unlocked(self):
    '''checks to see if the door was unlocked, returns true if it is, false otherwise'''
    return self._bolt_1_state.lower() == 'unlocked' and self._bolt_2_state.lower() == 'unlocked'

  def clue(self): 
    '''returns the hint that is returned if the user was unsuccessful at their attempt'''
    if self._bolt_2_state == 'unlocked' or self._bolt_1_state == 'unlocked':
      return 'You jiggle the door...it seems like one of the bolts is unlocked.'
    else:
      return '...it seems like it\'s completely locked'

  def success(self):
    '''returns the congratulatory message if the user was successful'''
    return 'Congratulations! You opened the door.'


