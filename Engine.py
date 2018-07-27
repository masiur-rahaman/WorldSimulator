from Character import Character
import random
from Actor import Actor
from UnHappyInputs import UnHappyInputs
from State import State

NUM_CHARACTERS = 5


class Engine:
    def __init__(self):
        pass

    def _seed(self, characters):
        character = random.choice(characters)
        character.set_react(random.choice(list(UnHappyInputs)))

    def start(self):
        characters = [Character(State.NEUTRAL, count) for count in xrange(4)]
        actor = Actor()
        actor.register_characters(characters)
        for character in characters:
            character.set_actor(actor)
        for character in characters:
            character.start()
        self._seed(characters)


if __name__ == '__main__':
    engine = Engine()
    engine.start()
