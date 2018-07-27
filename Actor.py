from State import State
import random
from HappyInputs import HappyInputs
from UnHappyInputs import UnHappyInputs


class Actor:
    def __init__(self):
        self._characters = None
        self._actor = {State.ANGRY: self.act_on_anger,
                       State.HAPPY: self.act_on_happiness,
                       State.NEUTRAL: self.act_on_neutral}

    def register_characters(self, characters):
        self._characters = characters

    def get_random_character(self):
        return random.choice(self._characters)

    def act_on_anger(self):
        random_character = self.get_random_character()
        random_character.set_react(random.choice(list(UnHappyInputs)))

    def act_on_happiness(self):
        random_character = self.get_random_character()
        random_character.set_react(list(HappyInputs))

    def act_on_neutral(self):
        pass

    def act(self, state):
        self._actor[state]()
