import door
import random

class BasicDoor(door.Door):
  '''Creates a door that needs to be pushed or pulled
   Attributes:
   1.State of the door(Push or Pull)
   2.List of choices for the state of the door
   3.Users input
  '''
  
  def __init__(self):
    '''initializes the door to be pushed or pulled'''
    self.choices = ['Push', 'Pull']
    self._state = random.choice(self.choices)
    self._input = None
  
  def examine_door(self):
    '''Returns a string description of the door'''
    return 'A door that is either pushed or pulled.'

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
    self._input = self.choices[option - 1]
    return f'You attempt to {self.choices[option - 1].lower()} the door'

  def is_unlocked(self):
    '''checks to see if the door was unlocked, returns true if it is, false otherwise'''
    return self._state.lower() == self._input.lower()

  def clue(self):
    '''returns the hint that is returned if the user was unsuccessful at their attempt'''
    return 'Try the other way.'

  def success(self):
    '''returns the congratulatory message if the user was successful'''
    return 'Congratulations! You opened the door.'
    