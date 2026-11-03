"""zoo animal class hierarchy and enclosures."""


class Animal:
    """Base class for available zoo animal."""

    def __init__(self, name: str, species: str) -> None:
        self.name = name
        self.species = species

    def speak(self) -> str:
        return "Animal sound"


class Mammal(Animal):
    """Mammal class inheriting from Animal."""

    def give_birth(self) -> str:
        return f"{self.name} the {self.species} has given birth"


class Bird(Animal):
    """Bird class inheriting from Animal with wingspan."""

    def __init__(self, name: str, species: str, wingspan: float) -> None:
        super().__init__(name, species)
        self.wingspan = wingspan


class Reptile(Animal):
    """Reptile class inheriting from Animal."""

    def bask_in_sun(self) -> str:
        return f"{self.name} the {self.species} is basking in the sun"


class Primate(Mammal):
    """Primate class inheriting from Mammal."""

    def climb_trees(self) -> str:
        return f"{self.name} the {self.species} is climbing trees"


class Marsupial(Mammal):
    """Marsupial class inheriting from Mammal."""

    def carry_baby(self) -> str:
        return f"{self.name} the {self.species} is carrying its baby"


class Aviary:
    """Enclosure designated for birds."""

    def __init__(self, birds: list | None = None) -> None:
        self.birds: list = birds if birds is not None else []


class ReptileEnclosure:
    """Enclosure designated for reptiles."""

    def __init__(self, reptiles: list | None = None) -> None:
        self.reptiles: list = reptiles if reptiles is not None else []