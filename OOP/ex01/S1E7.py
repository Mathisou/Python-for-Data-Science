from S1E9 import Character


class Baratheon(Character):
    """Class representing a Baratheon character."""
    def __init__(self, first_name, is_alive=True):
        """Initialize a Baratheon character with a name and alive status."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """Return a string representation of the Baratheon character."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """
        Return an official string representation
        of the Baratheon character.
        """
        return self.__str__()

    def die(self):
        """Mark the Baratheon character as dead."""
        self.is_alive = False


class Lannister(Character):
    """Class representing a Lannister character."""
    def __init__(self, first_name, is_alive=True):
        """Initialize a Lannister character with a name and alive status."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """Return a string representation of the Lannister character."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """
        Return an official string representation
        of the Lannister character.
        """
        return self.__str__()

    def die(self):
        """Mark the Lannister character as dead."""
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """Create a Lannister character with a name and alive status."""
        instance = cls(first_name)
        instance.is_alive = is_alive
        return instance
