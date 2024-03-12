from enum import auto
from strenum import StrEnum


class AnimalEnum(StrEnum):
    DOG = auto()
    CAT = auto()


class Register:
    animals = {}

    @classmethod
    def register_task(cls, task_name):
        def decorator(handler_class):
            if task_name in cls.animals:
                raise ValueError(f"Task '{task_name}' is already registered.")
            cls.animals[task_name] = handler_class
            return handler_class

        return decorator

    def get_task(self, enum):
        return self.animals[enum]()


class Animal:
    def speak(self):
        raise NotImplementedError(f"{self.__class__.__name__} speak is not implemented")


@Register.register_task(AnimalEnum.DOG)
class Dog(Animal):
    def speak(self):
        return "Woof!"


@Register.register_task(AnimalEnum.CAT)
class Cat(Animal):
    def speak(self):
        return "Meow!"


class AnimalFactory:
    def __init__(self):
        self.register = Register()

    def create_animal(self, enum):
        return self.register.get_task(enum)


def main():
    animal_factory = AnimalFactory()

    cat = animal_factory.create_animal(AnimalEnum.CAT)
    print(cat.speak())
    dog = animal_factory.create_animal(AnimalEnum.DOG)
    print(dog.speak())


if __name__ == "__main__":
    main()
