from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class representing a character."""

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Initialize a character with a name and alive status."""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Mark the character as dead."""
        pass


class Stark(Character):
    """Class representing a Stark character."""
    def __init__(self, first_name, is_alive=True):
        """Initialize a Stark character with a name and alive status."""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Mark the Stark character as dead."""
        self.is_alive = False
