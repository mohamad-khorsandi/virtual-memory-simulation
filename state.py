import enum

class State(enum.Enum):
    ready = 1
    running = 2
    blocked = 3