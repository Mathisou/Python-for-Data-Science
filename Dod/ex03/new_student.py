import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random ID composed of 15 lowercase letters."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    A class representing a student with various attributes.

    Attributes:
        name (str): The first name of the student.

        surname (str): The last name of the student.

        active (bool): Indicates if the student is
                       currently active. Defaults to True.

        login (str): The login identifier for the student,
                     generated from name and surname.

        id (str): A unique identifier for the student,
                  generated automatically.

    Methods:
        __post_init__: Runs after the dataclass is initialized to set the login
    """
    name: str = field(init=True)
    surname: str = field(init=True)
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False, default=generate_id())

    def __post_init__(self):
        self.login = f"{self.name[0].capitalize()}{self.surname.lower()}"
