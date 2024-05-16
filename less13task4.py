from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "гав гав!"

class Cat(Animal):
    def speak(self):
        return "мяу мяу!"

class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Unknown animal type")

if __name__ == "__main__":
    factory = AnimalFactory()

    animal_type = input("Введите тип животного (dog или cat): ").strip().lower()
    try:
        animal = factory.create_animal(animal_type)
        print(f"Животное говорит: {animal.speak()}")
    except ValueError as e:
        print(e)