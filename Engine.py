from Character import Character
import random
from Actor import Actor
from UnHappyInputs import UnHappyInputs
from HappyInputs import HappyInputs
from State import State

NUM_CHARACTERS = 4


class Engine:
    def __init__(self, result_accumulator):
        self._result_accumulator = result_accumulator
        pass

    def _seed(self, characters):
        character = random.choice(characters)
        character.set_react(random.choice(list(UnHappyInputs)))
        character = random.choice(characters)
        character.set_react(random.choice(list(HappyInputs)))

    def start(self):
        characters = [Character(State.NEUTRAL, count, self._result_accumulator) for count in xrange(NUM_CHARACTERS)]
        actor = Actor(self._result_accumulator)
        actor.register_characters(characters)
        for character in characters:
            character.set_actor(actor)
        for character in characters:
            character.start()
        self._seed(characters)


if __name__ == '__main__':
    engine = Engine()
    engine.start()
