import door
import random

class LockedDoor(door.Door):
  '''Creates a locked door and methods to help the user unlock it
     Attributes:
     1.Key location(Under mat, under flower pot, or under fake rock)
     2.List of choices for the key locations
     3.Users input
    '''
  
  def __init__(self):
    '''Initializes variables'''
    self.choices = ['Under the flower pot', 'Under the mat', 'Under the fake rock']
    self._state = random.choice(self.choices)
    self._input = None
    
  def examine_door(self):
    '''Returns a string description of the door'''
    return 'A locked door. Look around for the key'

  def menu_options(self):
    '''returns a string of the menu options that user can choose from when attmpting to unlock the door'''
    menu_options = ''
    for i, choice, in enumerate(self.choices):
      menu_options += f'{i + 1}. {choice}\n'
    return menu_options

  def get_menu_max(self):
    '''returns the number of options in the above menu'''
    return 3

  def attempt(self, option):
    '''passes in the user's selection from the menu. Uses that value to update the attributes that are needed to determine whether the user has unlocked the door. Return a string describing what the user atttempted'''
    self._input = self.choices[option - 1]
    if self.is_unlocked():
      return f'You look {self.choices[option - 1].lower()} and find the key!'
    else:
      return f'You look {self.choices[option - 1].lower()} and find nothing.'
  
  def is_unlocked(self):
    '''checks to see if the door was unlocked, returns true if it is, false otherwise'''
    return self._state.lower() == self._input.lower()

  def clue(self): 
    '''returns the hint that is returned if the user was unsuccessful at their attempt'''
    return 'Look somewhere else'

  def success(self):
    '''returns the congratulatory message if the user was successful'''
    return 'Congratulations! You opened the door.'