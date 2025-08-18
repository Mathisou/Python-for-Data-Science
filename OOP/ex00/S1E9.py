from abc import ABC, abstractmethod


class Character(ABC):
    """Base class for characters in a story."""
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """
        Initialize a character.

        Args:
            first_name (str): The first name of the character.
            is_alive (bool, optional): The character's life status. Defaults to True.
        """
        self.first_name = first_name
        self.is_alive = is_alive
    
    @abstractmethod
    def die(self):
        """Change the character's state to dead."""
        pass

class Stark(Character):
    """Class representing a character from the Stark family."""
    def __init__(self, first_name, is_alive=True):
        """Initialize a Stark character."""
        super().__init__(first_name, is_alive)

    def die(self):
        """Change the character's state to dead."""
        self.is_alive = False