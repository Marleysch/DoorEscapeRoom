import abc

class Door(abc.ABC):
  '''Door interface creating abstract methods'''
  @abc.abstractmethod
  def examine_door(self):
    '''Returns a string description of the door'''
    pass

  @abc.abstractmethod
  def menu_options(self):
    '''returns a string of the menu options that user can choose from when attmpting to unlock the door'''
    pass

  @abc.abstractmethod
  def get_menu_max(self):
    '''returns the number of options in the above menu'''
    pass

  @abc.abstractmethod
  def attempt(self, option):
    '''passes in the user's selection from the menu. Uses that value to update the attributes that are needed to determine whether the user has unlocked the door. Return a string describing what the user atttempted'''
    pass

  @abc.abstractmethod
  def is_unlocked(self):
    '''checks to see if the door was unlocked, returns true if it is, false otherwise'''
    pass
    
  @abc.abstractmethod
  def clue(self): 
    '''returns the hint that is returned if the user was unsuccessful at their attempt'''
    pass

  @abc.abstractmethod
  def success(self):
    '''returns the congratulatory message if the user was successful'''
    pass