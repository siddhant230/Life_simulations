class SimpleActor:
    def __init__(self, uid=None, action_space=None,
                 memory=None, relations=None):
        self.uid = uid
        self.action_space = action_space  # e.g., the ACTION_SET from Simulation
        self.memory = memory            # Instance of the Memory class
        self.relations = relations      # e.g., a dict mapping other UIDs to a relation type

    def act(self, world_state):
        """
        Determines the actor's next action based on the current state of the world
        and its own memory/relations.
        """
        # A simple deterministic action for illustration:
        if world_state.get('some_condition'):
            return 'FREE_WILL_CHOICE'
        else:
            return 'ACTION_SET[0]'

    def learn(self, old_state, action, new_state):
        """Updates internal state or memory based on a transition."""
        if self.memory:
            self.memory.add_experience(old_state, action, new_state)

    def update_relations(self):
        """Updates relationships with other actors."""
        pass
