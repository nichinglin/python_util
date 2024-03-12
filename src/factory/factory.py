import os, sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))


class Animal:
    def speak(self):
        raise NotImplementedError(f"{self.__class__.__name__} speak is not implemented")


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError(f"Invalid animal type: {animal_type}")


def main():
    # Example usage:
    animal_factory = AnimalFactory()

    dog = animal_factory.create_animal("dog")
    print(dog.speak())  # Output: Woof!

    cat = animal_factory.create_animal("cat")
    print(cat.speak())  # Output: Meow!


if __name__ == "__main__":
    main()
