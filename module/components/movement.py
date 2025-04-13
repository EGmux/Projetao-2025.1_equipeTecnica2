import pandas
import movement
import utils


class NegativeFramesToConsider(Exception):
    """Exception raised when the frames to consider are negative"""
    
    def __init__(self,context):
        super().__init__(f"negatives frame to consider in: {context}")

class FrameCantBeFound(Exception):
    """Exception raised when no frame in a sequence of frames implies a movement"""
    
    def __init__(self,context):
        super().__init__(f"no frames found in: {context}")


class Movement():

    def __init__(self, name="",feedback="", frames_to_consider = 0,starting_frame=None):
        self._starting_frame  = starting_frame
        self._frames_to_consider = frames_to_consider
        self._name = name
        self._feedback = feedback
        self._last_frame = self._starting_frame
        self._validated = False

    def starting_frame(self):
        """
        getter
        """
        return self._starting_frame

    def frames_to_consider(self):
        """
        getter
        """
        return self._frames_to_consider

    def validated(self):
        """
        getter
        """
        return self._validated



    def last_frame(self):
        """
        getter
        """
        return self._last_frame


    def _first_validation(self,df):
        """
        runs only if is the first time calling verify
        make sure that starting_frame and last_frame are the same
        """
        # Analysis module code
        self._last_frame = self.is_next_movement_present()
        self._starting_frame = self._last_frame
        self._last_frame = self._starting_frame
        return 

    def _trim_frames(self,df):
        """
        everytime the last frames_to_consider plus the last_frame offset results
        in a frame number higher than total ammount of frames this make sure 
        frames to consider is "trimmed"
        """
        total_frames = utils.total_frames(df)
        if self._last_frame + self._frames_to_consider > total_frames:
            # trim ammount of frames to fit df
            self._frames_to_consider = total_frames - self._last_frame

    def _analyze_frames(self,df):
        """
        check if filtered df has the next frame based on the logic provided by the Analysis module
        assuming it does update the state of last_frame otherwise raises FrameCantBeFound

        raises FrameCantBeFound
        """
        filtered_df = utils.filter_frames(df,self._last_frame,self._frames_to_consider)
        # Analysis module code
        is_present, next_frame = self.is_next_movement_present(filtered_df)

        if not is_present:
            raise FrameCantBeFound(f"{self._name}._analyze_frames")
        else:
            self._last_frame = next_frame

    def _find_next_frame(self,df):
        """
        if no frame has been validated before executes first_validation, returns if call to first_validation
        after than trims the frame if necessary
        finalizing by calling the exernal module Analysis to find the next frame
        """
        if self._starting_frame == None:
            self._first_validation(df)
            return

        self._trim_frames(df)

        self._analyze_frames(df)

    def verify(self,df):
        """
        verify that next movement can be found in a sequence of frames, assuming it does
        set the validated status of the movement to True, by default is False

        raises NegativeFramesToConsider and FrameCantBeFound
        """
        if self._frames_to_consider < 0:
            raise NegativeFramesToConsider(f"{self._name}.verify")
        try:
            self._find_next_frame(df)
        except FrameCantBeFound:
                return
        self._validated = True


 
