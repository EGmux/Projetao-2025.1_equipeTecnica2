from _pytest import monkeypatch
from _pytest.tmpdir import tmp_path, tmp_path_factory
from numpy import empty
import pytest
import pandas
import functools
import movement
import action


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



class TestVerifyMovement:

    def setup_method(self):
        self.action = action.Action()

    def test_empyt_collection_of_movements_by_default(self):
        assert len(self.action.movements()) == 0

    def test_success_state_by_default_false(self):
        assert self.action.validated() == False

    def test_verifying_empty_movement_collection_raises_exception(self):
        csv = test_csv()
        try:
            self.action.verify(csv)
        except action.EmptyMovementList:
            assert True
        else:
            assert False

    def test_non_matching_df_should_not_updated_success_for_action(self):
        movement = single_movement_provided()
        calls_cnt = utils.count_calls(monkeypatch,self.action, self.action.verify)
        self.action.add_movement(movement)
        df = test_csv()
        assert self.action.verify(df) == False and self.action.is_succesfull() == False and calls_cnt.get() == 1

    def test_matching_df_should_update_success_for_action(self):
        # como implementar esse?
        pass

    def test_verifying_empty_df_raises_exception(self):
        csv = empyt_csv()
        try:
            self.action.verify(csv)
        except action.EmptyMovementList:
            assert True
        else:
            assert False

    def test_verifying_df_with_less_frames_than_movements_raises_exception(self):
        df = test_csv()
        df_filtered = df.filter(items=['frame_number'],like='0')  # filter all rows with frame_number == 0
        movement = single_movement_provided()
        self.action.add_movement(movement)
        try:
            self.action.verify(df_filtered)
        except action.LessFramesThanMovements:
            assert True
        else:
            assert False

    def test_removing_from_movements_without_movement_raises_exception(self):
        try:
            self.action.remove_movement()
        except action.EmptyMovementList:
            assert True
        else:
            assert False



