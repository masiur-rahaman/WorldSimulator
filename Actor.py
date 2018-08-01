from State import State
import random
from HappyInputs import HappyInputs
from UnHappyInputs import UnHappyInputs
from logger import  log


class Actor:
    def __init__(self, result_accumulator):
        self._result_accumulator = result_accumulator
        self._characters = None
        self._actor = {State.ANGRY: self.act_on_anger,
                       State.HAPPY: self.act_on_happiness,
                       State.NEUTRAL: self.act_on_neutral}

    def register_characters(self, characters):
        self._characters = characters

    def get_random_character(self):
        return random.choice(self._characters)

    def act_on_anger(self, initiator_id):
        random_character = self.get_random_character()
        random_unhappy_input = random.choice(list(UnHappyInputs))
        # msg = str(initiator_id)+'----('+random_unhappy_input.name+')---->'+str(random_character.get_id())
        msg = '{from:'+str(initiator_id)+',action:\''+random_unhappy_input.name+'\',to:'+str(random_character.get_id())+'}'
        log(msg)
        self._result_accumulator.add(msg)
        random_character.set_react(random_unhappy_input)

    def act_on_happiness(self, initiator_id):
        random_character = self.get_random_character()
        random_happy_input = random.choice(list(HappyInputs))
        # msg = str(initiator_id)+'----('+random_happy_input.name+')---->'+str(random_character.get_id())
        msg = '{from:'+str(initiator_id)+',action:\''+random_happy_input.name+'\',to:'+str(random_character.get_id())+'}'
        log(msg)
        self._result_accumulator.add(msg)
        random_character.set_react(random_happy_input)

    def act_on_neutral(self, initiator_id):
        pass

    def act(self, initiator_id, state):
        self._actor[state](initiator_id)
