import pandas
import movement
import utils

class EmptyMovementList(Exception):
    """Exception raised when no movement is present in an action"""

    def __init__(self, context):
        super().__init__(f"tried to verify an empty movement list in: {context}")

class LessFramesThanMovements(Exception):
    """Exception raised when the df has less frames than ammount of movements"""

    def __init__(self, context):
        super().__init__(f"less frames than movements in: {context}")

class EmptyDF(Exception):
    """Exception raised when the df is empty"""
    
    def __init__(self,context):
        super().__init__(f"empty df in: {context}")

class Action:
    def __init__(self,movements=[],name="action is not named"):
        self._movements = movements
        self._is_successfull = False
        self._name = name

    def _empty_movement_list(self):
        """
        querier
        """
        return len(self._movements) == 0

    def add_movement(self, movement):
        """
        setter
        """
        self._movements.append(movement)

    def rename(self,new_name):
        """
        setter
        """
        if not new_name:
            # check if string is empty, pythonic
            raise ValueError('empty string')
        self._name = new_name


    def remove_movement(self, movement_number=None):
        """
        removes a movement from the movement list.
        if no movement_number is provided removes the last one
        """
        if self._empty_movement_list():
            raise EmptyMovementList(f"{self._name}.remove_movement")

        if movement_number is not None:
            self._movements.pop(movement_number)

        else:
            self._movements.pop()

    def movements(self):
        """
        getter
        """
        return self._movements

    def validated(self):
        """
        getter
        """
        return self._is_successfull

    def verify(self, df):
        """
        verify an action, verifying implies for each movement check if 
        the df has the frames that validate such movement.
        assuming each movement is validated update the action success state to True.

        raises EmptyMovementList, LessFramesThanMovements and EmptyDataError.
        """
        total_movements = len(self.movements())
        total_frames = util.total_frames(df)

        if total_movements == 0:
            raise EmptyMovementList(f"{self._name}.verify")
           
        if df.empty:
            raise EmptyDF(f"{self._name}.verify")
        
        if total_movements < total_frames:
            raise LessFramesThanMovements(f"{self._name}.verify")

        for current in range(total_movements):
            current_movement = self._movements[current]
            current_movement.verify(df)
            if not current_movement.validated():
                break

        self._is_successfull = True


            





    
    
