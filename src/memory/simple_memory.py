class SimpleVectorMemory:
    def __init__(self, max_size=1000):
        self.max_size = max_size
        # Stores tuples like (old_state, action, new_state)
        self.experiences = []

    def add_experience(self, old_state, action, new_state):
        """Adds a new experience to the memory buffer."""
        if len(self.experiences) >= self.max_size:
            # Simple FIFO (First-In, First-Out) eviction
            self.experiences.pop(0)
        self.experiences.append(
            {'old': old_state, 'action': action, 'new': new_state})

    def recall(self, query=None):
        """Retrieves information from memory (e.g., for learning or acting)."""
        if query is None:
            return self.experiences
        # Simple example of recalling the most recent experience
        return self.experiences[-1] if self.experiences else None
