class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"

    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"

    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.

        The robot starts at the first position and picks up the card.
        It has its light off.
        While it's not at the end of the list:
            It moves right.
            If the card it is holding is larger than the one it is at, it swaps the cards and turns its light on.
        When it's at the end of the list, it goes left until it reaches the beginning of the list.
            If its light is off, it swaps what is is holding with the first position (which would have nothing) and it returns  -- either its list, or nothing, since the test just looks at the value of its list.
            If its light is on, it turns off its light to reset it, moves over one position to the right and continues as before.

        Once it reaches the end of the list, it moves backwards and (maybe, probably not necessary, checks that the card is holds is smaller than
        the card at the position, (swapping if necessary and turning on it light)) until it reaches the position with no card. Then it 'swaps' the card with that position
        and moves one position right. And then continues until going back and forth doesn't make the light come on.

        Moves until it gets back to the hole. Then evaluate if light is on and move forward if it was.

        Maybe it if moves to the end and its light is off and swapping twice both is none (to show it holds nothing), return???
        """
        self.set_light_on()

        while self.light_is_on():
            self.set_light_off()

            # for i in range(0, len(self._list) - 1): # This is what I used BEFORE fully implementing the light
            # Pick up card
            self.swap_item()
            # Move right and compare as it goes.
            while(self.can_move_right()):
                self.move_right()
                if self.compare_item() == 1:
                    self.swap_item()
                    # print('swapping items')
                    self.set_light_on()
                    # print('turning light on')

            # Now, move left in the list to put the holding card in the hole.
            while(self.can_move_left()):
                self.move_left()
                if self.compare_item() == None:
                    self.swap_item()
                    break
            # print(self._list)

            # Move one position over before the loop starts again.
            self.move_right()

        # Stick the last card back in place
        while(self.can_move_right()):
            self.move_right()
        self.swap_item()
        return self._list


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1,
         45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)

    l2 = [1, 14, 2, 13]
    # robot2 = SortingRobot(l2)
    # robot2.sort()
    # print(robot2._list)
