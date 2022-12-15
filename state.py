import enum


class State(enum.Enum):
    ready = "ready"
    running = "running"
    blocked = "block"
