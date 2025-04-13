from _pytest import monkeypatch
from _pytest.tmpdir import tmp_path, tmp_path_factory
from numpy import empty
from pandas.core.indexers import utils
import pytest
import pandas
import functools
import movement
import utils as ut

@pytest.fixture
def single_movement_provided():
    # always return false  when treated as arg to the validator
    return (0,0,'passo1',False,0,'default')

@pytest.fixture
def test_csv():
    return pandas.read_csv("./test_data/output.csv")

@pytest.fixture
def empyt_csv():
    return pandas.DataFrame(list()).to_csv('empty.csv')

class TestVerifyStep:

    def setup_method(self):
        self.movement = movement.Movement()

    def test_starting_frame_must_be_less_or_equal_to_df_total_ammount_of_frames(self):
        df = test_csv()
        total_frames = ut.total_frames(df)
        self.movement.verify(df)
        starting_frame = 0
        if self.movement.starting_frame() == None:
            assert True
        elif self.movement.starting_frame() != None:
            starting_frame = self.movement.starting_frame()
        assert starting_frame  <= total_frames

    def test_starting_frame_must_be_positive_number(self):
        df = test_csv()
        starting_frame  = self.movement.starting_frame(df)
        if starting_frame != None:
            assert starting_frame >= 0
        else:
            assert True

    def test_default_starting_frame_is_zero(self):
        assert self.movement.starting_frame() == 0

    def test_default_frames_to_consider_are_zero(self):
        assert self.movement.frames_to_consider() == 0

    def test_frames_to_consider_plus_starting_frame_at_most_equal_to_total_frames(self):
        df = test_csv()
        total_frames = ut.total_frames(df)
        extra_frames = total_frames+1
        self.movement._frames_to_consider = extra_frames
        self.movement.verify(df)
        assert self.movement.frames_to_consider() == total_frames

    def test_after_starting_frame_found_last_frame_is_starting_frame(self):
        df = test_csv()
        starting_frame = self.movement.verify(df)
        self.movement.verify(df)
        last_frame = self.movement.last_frame()
        assert last_frame == starting_frame

    def test_after_finding_frame_distinct_from_starting_frame_last_frame_is_distinct_frame_number(self):
        df = test_csv()
        self.movement.verify(df)
        penultimate_frame = self.movement.last_frame()
        assert penultimate_frame < last_frame

    def test_default_success_state_is_false(self):
        assert self.movement.validated() == False

    def test_first_frame_is_penultimate_frame_of_df_and_frame_to_consider_is_one_is_valid(self):
        # how to test this
        pass

    def test_first_frame_is_last_frame_of_df_and_no_extra_frames_is_valid(self):
        # how to test this
        pass
