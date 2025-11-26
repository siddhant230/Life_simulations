import numpy as np
from src.actors.simple_actor import SimpleActor
from src.memory.simple_memory import SimpleVectorMemory


class SimpleVectorWorld:
    def __init__(self, N, ACTION_SET):
        self.N = N
        self.ACTION_SET = ACTION_SET
        # The main state array representing the deterministic background
        self.initial_states = np.random.choice(self.ACTION_SET, size=self.N)
        # Array to store the CURRENT state, which Actors can modify
        self.current_states = self.initial_states.copy()
        self.actors = {}  # Dictionary of Actor instances {uid: Actor instance}

    def initialize_actors(self):
        """Creates the initial set of actors."""
        for i in range(self.N):
            # Each actor gets an ID, the action space, and a memory object
            self.actors[i] = SimpleActor(uid=i, action_space=self.ACTION_SET,
                                         memory=SimpleVectorMemory(max_size=50))

    def get_state(self):
        """Returns the observable state of the world."""
        return self.current_states

    def update_state(self, actor_index, new_action):
        """An actor modifies the world state at their corresponding index."""
        if 0 <= actor_index < self.N:
            old_action = self.current_states[actor_index]
            self.current_states[actor_index] = new_action
            return old_action
        return None
