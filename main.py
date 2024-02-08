#Marley Schneider, Rene Trujillo
#10/16/23
#Program that simulates an escape room with different doors
import basicdoor
import lockeddoor
import deadboltdoor
import check_input
import random


#function for the user to attempt to open the door
def open_door(door):
  print(door.examine_door())
  #loops until the door is opened
  while True:
    print()
    user_selection = check_input.get_int_range(door.menu_options(), 1, door.get_menu_max())
    print(door.attempt(user_selection))
    # checks if door has been opened
    if door.is_unlocked():
      print(door.success())
      break
    else:
      print(door.clue())


# main function
def main():
  # list of doors to randomly choose from
  doors = [basicdoor.BasicDoor(), lockeddoor.LockedDoor(), deadboltdoor.DeadboltDoor()]
  # loops 3 times for 3 doors
  for _ in range(3):
    door = random.choice(doors)
    open_door(door)
  # once the loop finishes that means all doors have been opened, displays a congratulatory message
  print('Congratulations, you opened all the doors and escaped!')

main()