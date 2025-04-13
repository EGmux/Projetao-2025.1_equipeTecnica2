from _pytest.tmpdir import tmp_path, tmp_path_factory
import pytest
import pandas
import coach
import movement

    
@pytest.fixture
def single_action_provided():
    return ([],"remada",False)

@pytest.fixture
def single_action_provided_2():
    return ([],"ollie",False)



class TestPresentActions:

    def setup_method(self):
        self.coach = coach.Coach()

    def test_no_action_provided_by_default(self):
        actions = self.coach.get_actions()
        assert len(actions) == 0

    def test_single_action_provided_when_adding_a_single_action(self):
        action = single_action_provided()

        self.coach.add_action(action)
        actions = self.coach.get_actions()

        assert len(actions) == 1 and action == actions

    def test_no_action_left_when_deleting_last_action_from_collection_of_actions(self):
        action = single_action_provided()
        actionID = 0

        self.coach.add_action(action)
        self.coach.remove_action(actionID)
        actions = self.coach.get_action()

        assert len(actions) == 0

    def test_exception_raised_when_deleting_from_empty_collection_of_actions(self):
        actionID = 0
        try: 
            self.coach.remove_action(actionID)
        except coach.EmptyActionList:
            assert True
        else:
            assert False

    def test_single_action_removed_when_removing_a_single_action(self):
        first_action = single_action_provided()
        second_action = single_action_provided_2()
        actionID = 0

        self.coach.add_action(first_action)
        self.coach.add_action(second_action)
        self.coach.remove_action(actionID)
        actions  = self.coach.get_actions()

        assert len(actions) == 1 and actions == second_action

class TestConvertVideoToDF:
    # código de Pedro, não vamos testar, só copiar e colar por enquanto
    pass

class TestVerifyAction:

    def setup_method(self):
        self.coach = coach.Coach()

    def test_exception_raised_when_action_not_present_in_actions_collection(self):
        action = single_action_provided()

        self.coach.add_action(action)

        try: 
            self.coach.get_action('ollie')  
        except coach.ActionNotPresent:
            assert True
        else:
            assert False

    def test_action_present_in_actions_collection(self):
        action = single_action_provided()

        self.coach.add_action(action)
        assert self.coach.getAction('remada') == action

    def test_df_empty_by_default(self):
        assert len(self.coach.getDF()) == 0



class TestProvideFeedback:

    def setup_method(self):
        self.coach = coach.Coach()

    def test_create_out_path_if_not_present(self):
        out_path = tmp_path / "./test_data/out.feed"
        try:
            self.coach.provide_feedback()
        except FileNotFoundError:
            self.coach.create_feedback_path(out_path)
        else:
            assert False
        assert self.coach.provide_feedback() == True

    def test_when_df_is_empty_raise_exception(self):
        try:
            self.coach.provide_feedback()
        except coach.DFIsEmpty:
            assert True
        else:
            assert False

   
    
