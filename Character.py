from Machine import Machine
import time
from State import State
import threading
from HappyInputs import HappyInputs
from UnHappyInputs import UnHappyInputs
from logger import log


class Character(Machine, ):
    def __init__(self, state, identity, result_accumulator):
        self._result_accumulator = result_accumulator
        self._id = identity
        self._curr_state = state
        self._actor = None
        self._state_transition = {UnHappyInputs.SLAP: State.ANGRY,
                                  UnHappyInputs.SLANG: State.ANGRY,
                                  HappyInputs.KISS: State.HAPPY,
                                  HappyInputs.PRAISE: State.HAPPY}
        self._color_switcher = {State.ANGRY: 'RED',
                                State.HAPPY: 'GREEN',
                                State.NEUTRAL: 'BLUE'}

        self._act = threading.Thread(target=self.act, args=())
        self._show_color = threading.Thread(target=self.show_color, args=())
        # t1.start()
        # t2.start()
        # t3.start()
        # t1.join()
        # t2.join()
        pass

    def get_id(self):
        return self._id

    def set_actor(self, actor):
        self._actor = actor

    def start(self):
        self._act.start()
        self._show_color.start()

    def set_state(self, state):
        self._curr_state = state

    def show_color(self):
        while 1:
            msg = str(self._id) + '::' + self._color_switcher.get(self._curr_state)
            log(msg)
            # self._result_accumulator.add(msg)
            time.sleep(5)

    def act(self):
        while 1:
            self._actor.act(self._id, self._curr_state)
            time.sleep(5)

    def set_react(self, react):
        self.set_state(self._state_transition[react])
